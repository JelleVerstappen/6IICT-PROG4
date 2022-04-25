import RPi.GPIO as GPIO # Only works on Raspberry Pi
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

while True:
    print("Even on, Odd off")
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(12 ,GPIO.HIGH)
    GPIO.output(5 ,GPIO.LOW)

    time.sleep(1)

    print("Even off, Odd on")
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(12 ,GPIO.LOW)
    GPIO.output(5 ,GPIO.HIGH)

    time.sleep(1)
