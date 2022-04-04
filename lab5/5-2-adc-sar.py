import RPi.GPIO as GPIO
import time

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


dac = [26,19,13,6,5,11,9,10]
troyka = 17
bits=len(dac)
levels=2**bits
maxVoltage = 3.3
comparator = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)


try:
    while True:
        
        left = 0
        right = 64
        value = 32

        while right - value != 1:
            signal = num2dac(value)
            time.sleep(0.007)
            comparatorValue = GPIO.input(comparator)
            if comparatorValue:
                left = value
                value += (right - value)//2
            else:
                right = value
                value -= (value-left)//2
        voltage = value / levels * maxVoltage
        print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(dac, 0)
    GPIO.cleanup() 
    #print(decimal2binary(bits), "\n", bits+20)