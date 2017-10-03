#Program cycles colors

import time, sys
import RPi.GPIO as GPIO

redPin = 11   #Set to appropriate GPIO
greenPin = 13 #Should be set in the 
bluePin = 15  #GPIO.BOARD format

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
print("""Ensure the following GPIO connections: R-11, G-13, B-15""")

def main():
    GPIO.setmode(GPIO.BOARD)
    pins= (redPin, greenPin, bluePin)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    r= GPIO.PWM(redPin, 50)
    g= GPIO.PWM(greenPin, 50)
    b= GPIO.PWM(bluePin, 50)
    rgb=[r,g,b]
    try:
        for c in rgb:
            c.start(100)
        i=0
        while True:
            ca= rgb[i]
            i= (i+1)%3
            cz= rgb[i]
            for dc in range(0, 101, 1):
                cz.ChangeDutyCycle(100-dc)
                ca.ChangeDutyCycle(0+dc)
                time.sleep(0.1)
            time.sleep(5)
    except KeyboardInterrupt:
        for c in rgb:
            c.stop()
        GPIO.cleanup()
    return

main()

