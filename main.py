import serial
from time import sleep, time
import subprocess

rSer = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=3)
lSer = serial.Serial('dev/tty.SLAB_USBtoUART32', 115200)
print("serial connections made")

##Add file opener here
keys = getKeys()
lastPlayed = 'start'
readTime= time()
while True:
    nowPlaying = rSer.readline().decode().replace(' ','').strip()
    sleep(.1)
    print(nowPlaying)
    if (nowPlaying == lastPlayed):
    #print("lastPlayed is the same as now playing: " + lastPlayed)
            print("#####" * 10)
            stillPlaying()
            continue
    elif (nowPlaying in keys):
        print("Playing New Song")
        lSer.write('0'.encode('ascii'))
        print("nowPlaying is: " + nowPlaying)
        #os.system('omxplayer -o alsa /usr/share/sounds/alsa/Front_Center.wav')
    elif (nowPlaying == 'n'):
        lSer.write('3'.encode('ascii'))
        print('stop')
    lastPlayed = nowPlaying


def stopPlaying():
    ##Sends stop signal to lights "1"
    ##Kills OMX player
    pids = subprocess.check_output('ps cax | grep omxplayer')
    pids1 = pids.split()
    for pid in pids1:
        subprocess.check_output("kill "+ pid)
    lSer.write('1'.encode('ascii'))
    

def startPlaying(rfid):
    ##Searches RFID ID
    ##Sends newRecord "0"
    ##starts OMX Player
    loc = getTrack(rfid)
    os.system('omxplayer -o alsa' + loc)

def stillPlaying():
    ##Checks ps to see if OMX player still running
    ##sends Circle Signal "2"
    pids = subprocess.check_output('ps cax | grep omxplayer')
    if !(pids == ''):
        lSer.write('2'.encode('ascii'))
    else: lSer.write('1'.encode('ascii'))

def idleState():
    ##Sends idle signal
    lSer.write('3'.encode('ascii'))

def getTrack(key):
    loc = ''
    with open('records.csv') as file:
        data = file.readlines()
        for line in data:
            line1 = line.split(',')
            if (key == line1[1].strip().replace(" ", "")):
                loc = line1[2]
    print(loc)
    return loc

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
    