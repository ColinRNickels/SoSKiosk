import serial
from time import sleep, time
import os

<<<<<<< HEAD
rfidSerial = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=3)
neoPixel
print("serial connection made")
=======
ser = serial.Serial('/dev/ttyUSB0', 9600)
print("Serial Started")
counter = 32
>>>>>>> refs/remotes/origin/master

keys = ["0416DD324C5881", "04278572585881"]
lastPlayed = 'start'
readTime= time()
while True:
<<<<<<< HEAD
    nowPlaying = ser.readline().decode().replace(' ','').strip()
    # if (nowPlaying == ''):
    #     print("Newlined")
    #     nowPlaying = 'n'
    # print(readTime)
=======
    counter +=1
    print(ser.readline())
    nowPlaying = ser.readline().decode().replace(' ','').strip()
    sleep(.1)
    print('got nothing')
>>>>>>> refs/remotes/origin/master
    print(nowPlaying)
    sleep(.1)
    if (nowPlaying == lastPlayed):
            print("lastPlayed is the same as now playing: " + lastPlayed)
            print("#####" * 10)
            continue
    elif (nowPlaying in keys):
        print("Playing New Song")
        ser.write('0'.encode('ascii'))
        print("nowPlaying is: " + nowPlaying)
        #os.system('omxplayer -o alsa /usr/share/sounds/alsa/Front_Center.wav')
    elif (nowPlaying == 'n'):
        ser.write('3'.encode('ascii'))
        print('stop')
    lastPlayed = nowPlaying


def stopPlaying:
    ##Sends stop signal to lights "1"
    ##Kills OMX player

def startPlaying(rfid):
    ##starts OMX Player
    ##Searches RFID ID
    ##Sends newRecord "0"

def stillPlaying:
    ##Checks ps to see if OMX player still running
    ##sends Circle Signal "2"

def idleState:
    ##Sends idle signal
    