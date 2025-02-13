import serial
from time import sleep, time
import subprocess
import os
from gpiozero import DigitalOutputDevice

resetter = DigitalOutputDevice(16, initial_value=True) #connected to pin2 on ESP32 Board, when pulled low trigger reset.


def stillPlaying():
    ##Checks ps cax to see if OMX player still running
    ##sends Circle Signal "2"
	try:
		output = subprocess.check_output("ps cax | grep omxplayer", shell=True, stderr=subprocess.STDOUT)
		output = output.decode('ascii').split()
		lSer.write('2'.encode('ascii'))
		print("Still Playing")
		return True
	except subprocess.CalledProcessError:
		print("no longer playing stillPlaying = False")
		
		return False

def idleState():
    ##Sends idle signal
    print("Idle")
    lSer.write('3'.encode('ascii'))

def playTrack(key):
	loc = ''
	with open('/home/pi/SoSKiosk/records.csv') as file: #need to use full file location
		data = file.readlines() 
		for line in data:
			line1 = line.split(',')
			if (key == line1[1].strip().replace(" ", "")):
				loc = line1[2].strip()
				command = "omxplayer -o both /home/pi/SoSKiosk/songs/" + loc
	subprocess.Popen(command, shell=True)
	
def getKeys():
    ##Opens file, returns list of all keys
    keys = []
    with open('/home/pi/SoSKiosk/records.csv') as file:
        data = file.readlines()
        for line in data:
            line1 = line.split(',')
            keys.append(line1[1].strip().replace(" ", ""))
    print(keys)
    return keys
    
def stopPlaying():
    ##Sends stop signal to lights "1"
    ##Kills OMX player
	try:
		output = subprocess.check_output("ps cax | grep omxplayer", shell=True, stderr=subprocess.STDOUT)
		output = output.decode('ascii').split()
		for item in output:
			if item.isdigit():
				subprocess.call('kill ' + item, shell=True)
				#print("Killed " + item)
		lSer.write('1'.encode('ascii'))
	
	except subprocess.CalledProcessError:
		lSer.write('1'.encode('ascii'))

def connectRFIDSerial():
	rSer = serial.Serial('/home/pi/ttyRFID', 115200, timeout=.3)
	print("serial connections made")
	return rSer

def connectLEDSerial():
	lSer = serial.Serial('/home/pi/ttyLED', 115200)
	print("serial connections made")
	return lSer



def closeSerial():
	lSer.close()
	rSer.close()

rSer = connectRFIDSerial()
lSer = connectLEDSerial()

keys = getKeys()
lastPlayed = 'start'
readTime= time()
idleState()
resetCount = 0 
while True:
	if (lastPlayed == 'start'):
		idleState()
	try:
		nowPlaying = rSer.readline().decode().replace(' ','').strip()
	except:
		print("nowPlaying = " + nowPlaying)
	if (nowPlaying == 'nothing'):
		print("NONE NONE NONE NONE")
		nowPlaying = ''
	sleep(.2)
	if (nowPlaying == lastPlayed):
		print("lastPlayed is the same as now playing: " + lastPlayed)
		print("#####" * 10)
		if (nowPlaying == ''):
			idleState()
			nowPlaying = ''
		elif stillPlaying():
			continue
		else:
			lSer.write('1'.encode('ascii'))

	elif (nowPlaying in keys):
		print("Playing New Song")
		lSer.write('0'.encode('ascii'))
		playTrack(nowPlaying)
		print("nowPlaying is: " + nowPlaying)
	elif (nowPlaying == ''):
		if stillPlaying():
			print("Called Stop Playing")
			stopPlaying()
			nowPlaying = ''
		
	lastPlayed = nowPlaying
	resetCount +=1
	print(resetCount)
	if (resetCount % 500 == 0):
		closeSerial()
		rSer = connectRFIDSerial()
		lSer = connectLEDSerial()
		resetter.off()
		sleep(.05)
		resetter.on()

