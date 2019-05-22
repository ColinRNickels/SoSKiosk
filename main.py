import serial
from time import sleep, time
import subprocess
import os

def findSerials():
	listOfSerials = []
	output = subprocess.check_output('ls /dev/ | grep ttyUSB', shell=True)
	listOfSerials = output.decode('ascii').split()
	print(listOfSerials)
	return listOfSerials

def startPlaying(rfid):
    ##Searches RFID ID
    ##Sends newRecord "0"
    ##starts OMX Player
    loc = getTrack(rfid)
    subprocess.call('omxplayer -o alsa' + loc)

def stillPlaying():
    ##Checks ps cax to see if OMX player still running
    ##sends Circle Signal "2"
	try:
		output = subprocess.check_output("ps cax | grep omxplayer", shell=True, stderr=subprocess.STDOUT)
		output = output.decode('ascii').split()
		lSer.write('2'.encode('ascii'))
		return True
	except subprocess.CalledProcessError:
		print('Not Running')
		lSer.write('1'.encode('ascii'))
		return False

def idleState():
    ##Sends idle signal
    lSer.write('3'.encode('ascii'))

def playTrack(key):
	loc = ''
	with open('records.csv') as file:
		data = file.readlines()
		for line in data:
			line1 = line.split(',')
			if (key == line1[1].strip().replace(" ", "")):
				loc = line1[2].strip()
				#print(loc)
				command = "omxplayer -o both /home/pi/SoSKiosk/songs/" + loc
				print(command)
	subprocess.Popen(command, shell=True)
	#os.system(command)
	
def getKeys():
    ##Opens file, returns list of all keys
    keys = []
    with open('records.csv') as file:
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
	#print(output)
		for item in output:
			if item.isdigit():
				subprocess.call('kill ' + item, shell=True)
				print("Killed " + item)
		lSer.write('1'.encode('ascii'))
	except subprocess.CalledProcessError:
		print('Not Running')
		lSer.write('1'.encode('ascii'))
		    

serials = findSerials()
rSer = serial.Serial('/dev/' + serials[1], 115200, timeout=1.5)
lSer = serial.Serial('/dev/' + serials[0], 115200)
print("serial connections made")


keys = getKeys()
lastPlayed = 'start'
readTime= time()
while True:
	nowPlaying = rSer.readline().decode().replace(' ','').strip()
	sleep(.2)
	print(nowPlaying)
	if (nowPlaying == lastPlayed):
	#print("lastPlayed is the same as now playing: " + lastPlayed)
		print("#####" * 10)
		if (nowPlaying == ''):
			idleState()
		elif stillPlaying():
			continue
	elif (nowPlaying in keys):
		print("Playing New Song")
		lSer.write('0'.encode('ascii'))
		playTrack(nowPlaying)
		print("nowPlaying is: " + nowPlaying)
	elif (nowPlaying == ''):
		stopPlaying()
	lastPlayed = nowPlaying



		

