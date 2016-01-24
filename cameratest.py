#!/usr/bin/python
# picamera trial  - class version

import picamera
import RPi.GPIO as GPIO
import time
PIN = 4
DESTIN = '/home/pi/Pictures/img'
LOGFILE = '/home/pi/master/camera/log/camera.log'

class Camera:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIN,GPIO.IN)
		camera = picamera.PiCamera()
		camera.resolution = (1024,768)
		# camera.capture('/home/pi/Pictures/image.jpg')
		print 'Camera test'
		print 'Camera initialised'
		print 'Storing photos in ',DESTIN
		print 'Use scp to copy photos back to c:\andyt\mydocuments\github\photos'
		print 'Issue: transferring photos is triggering more photos - maybe need to screen wifi stick'
		camera.start_preview()		# only on the directly connected monitor
		time.sleep(2)

	def continuous(self):
		try:
			for filename in camera.capture_continuous('/home/pi/Pictures/img{counter:03d}.jpg'):
				print('Captured %s' % filename)
				while GPIO.input(PIN) == False:
					time.sleep(2)
		except:			# ctrl-c, tidy up
				camera.stop_preview()
				print 'Tidying up'
		
	def single_shot_loop(self):
		''' Currently capturing double shots.'''
		i = 0
		print 'Entering infinite loop'
		while True:
			print 'Waiting for gpio'
			while GPIO.input(PIN) == False:
				time.sleep(.1)
			snap(i)
			time.sleep(.5)
			snap(i)
			time.sleep(1)
			
	def snap(self, i):
		filename = DESTIN+str(i)+'.jpg'
		i += 1
		camera.capture(filename)
		print('Captured %s' % filename)
	
if __name__ == "__main__":
	'''	camera main routine
		Sets up the logging and constants, before calling ...
	'''
#	logging.basicConfig(format='%(levelname)s:%(message)s',
	logging.basicConfig(
						filename=LOGFILE,
						filemode='w',
						level=logging.INFO)	#filemode means that we do not append anymore
#	Default level is warning, level=logging.INFO log lots, level=logging.DEBUG log everything
	logging.warning(datetime.datetime.now().strftime('%d %b %H:%M')+". Running camera class as a standalone app")
	single_shot_loop()	

	