#!/usr/bin/python
# picamera trial

import picamera
import RPi.GPIO as GPIO
import time
PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN)
DESTIN = '/home/pi/Pictures/img'
camera = picamera.PiCamera()
camera.resolution = (1024,768)
# camera.capture('/home/pi/Pictures/image.jpg')
print 'Camera test'
print 'Camera initialised'

camera.start_preview()		# only on the directly connected monitor
time.sleep(2)
#try:
#	for filename in camera.capture_continuous('/home/pi/Pictures/img{counter:03d}.jpg'):
#		print('Captured %s' % filename)
#		while GPIO.input(PIN) == False:
#			time.sleep(2)
#except:			# ctrl-c, tidy up
#		camera.stop_preview()
#		print 'Tidying up'
		
i = 0
print 'Entering infinite loop'
while True:
	print 'Waiting for gpio'
	while GPIO.input(PIN) == False:
		time.sleep(.1)
	filename = DESTIN+str(i)+'.jpg'
	i += 1
	camera.capture(filename)
	print('Captured %s' % filename)
	time.sleep(1)
		