import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14,GPIO.IN)

while True:
    print(GPIO.input)  