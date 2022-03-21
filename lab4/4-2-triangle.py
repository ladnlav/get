import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26,19,13,6,5,11,9,10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

T=6
try:
    while True:
        for x in range(0,256):
            Volt=(3.3*x/256)
            number = dec2bin(x)
            GPIO.output(dac,number)
            time.sleep(T/2/512)
            
        for x in range(255,-1,-1):
            Volt=(3.3*x/256)
            number = dec2bin(x)
            GPIO.output(dac,number)
            time.sleep(T/2/512)
            
        break


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 
