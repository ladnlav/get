import RPi.GPIO as GPIO

def notdigit(str):
    if str.isdigit():
        return 0
    else:
        try:
            float(str)
            return 1
        except ValueError():
            return 1

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26,19,13,6,5,11,9,10]
num = [0,0,0,0,0,0,0,0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        i = input("Введите целочисленное число от 0 до 255 или q для выхода:")
        if i == 'q':
            break
        elif notdigit(i):
            print("Ведено не целочисленное значение")
        elif int(i) < 0:
            print ("Значение должно быть больше 0")
        elif int(i) > 255:
            print ("Значение должно быть в диапазоне от 0 до 255")
        else:
            bits = decimal2binary(int(i))
            
            k=0
            ratio = 0.5
            voltage = 0
            for x in bits:
                voltage = voltage +3.3*x*ratio
                ratio=ratio/2
        #bits = int(input("Введите целочисленное число от 0 до 255 или q для выхода:"))
        GPIO.output(dac, bits)
        print(bits,voltage)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup() 
    #print(decimal2binary(bits), "\n", bits+20)