#!/usr/bin/python
# gpio test

import RPi.GPIO as GPIO
import time
PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)
while True:
	print GPIO.input(PIN)
	time.sleep(1)
	