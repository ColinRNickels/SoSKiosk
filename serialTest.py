#serialtest.py
import serial
from time import sleep, time
import subprocess
import os


def connectRFIDSerial():
	rSer = serial.Serial('/home/pi/ttyRFID', 115200, timeout=1)
	print("serial connections made")
	return rSer
	
rSer = connectRFIDSerial()
while True:
	print(rSer.readline().decode().replace(' ','').strip())
