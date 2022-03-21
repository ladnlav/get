import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)


GPIO.output(27, 1)
time.sleep(1)
 
GPIO.output(27, 0)
time.sleep(1)

GPIO.output(27, 1)
time.sleep(1)
 
GPIO.output(27, 0)
time.sleep(1)

GPIO.output(27, 1)
time.sleep(1)
 
GPIO.output(27, 0)
time.sleep(1)

GPIO.output(27, 1)
time.sleep(1)
 
GPIO.output(27, 0)
time.sleep(1)
GPIO.cleanup() 
