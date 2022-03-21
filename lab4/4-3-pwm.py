import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p=GPIO.PWM(22,1000)

try:
    while True:
        dc=input("Введите коэффициент заполнения ШИМ")
        p.start(int(dc))
        input("Press return to stop:")
        p.stop()
finally:
    GPIO.cleanup()
