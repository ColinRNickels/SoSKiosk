import serial
from time import sleep
from gpiozero import LED
import os

ser = serial.Serial('/dev/ttyUSB0', 115200)
counter = 32

red =  LED(2)
green = LED(3)

def flashStart(led):
    led.blink(.5,.5,3,True)
lastPlayed = 'n'
while True:
    counter +=1
    nowPlaying = ser.readline().decode().replace(' ','').strip()
    sleep(.1)
    print(nowPlaying)
    if (nowPlaying == lastPlayed):
        continue
    elif (nowPlaying == '0416DD324C5881'):
        print("equal")
        flashStart(green)
        os.system('omxplayer -o alsa /usr/share/sounds/alsa/Front_Center.wav')
    elif (nowPlaying == 'n'):
        flashStart(red)
        print('stop')
        
    lastPlayed = nowPlaying
    if counter == 255:
        counter = 32
