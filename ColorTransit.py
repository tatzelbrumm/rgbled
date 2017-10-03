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
    
print("""Ensure the following GPIO connections: R-11, G-13, B-15
Colors: Red, Green, Blue, Yellow, Cyan, Magenta, and White
Use the format: color on/color off""")

def main():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(redPin, GPIO.OUT)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.setup(bluePin, GPIO.OUT)
    r= GPIO.PWM(redPin, 50)
    g= GPIO.PWM(greenPin, 50)
    b= GPIO.PWM(bluePin, 50)
    r.start(100)
    g.start(100)
    b.start(100)
    return

main()

