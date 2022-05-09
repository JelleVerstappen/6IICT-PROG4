import RPi.GPIO as GPIO # Only works on Raspberry Pi
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

<<<<<<< HEAD
=======
while True:
    print("Even on, Odd off")
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(12 ,GPIO.HIGH)
    GPIO.output(5 ,GPIO.LOW)
>>>>>>> 9e2ce18b8d17bb262391c8ce84b121ac06be4dcd

class LED():
    def __init__(self, led):
      self.led = led
      GPIO.setup(self.led, GPIO.OUT)
      
      
    def on(self):
      GPIO.output(self.led, GPIO.HIGH)
      
    def off(self):
      GPIO.output(self.led, GPIO.LOW)
      
while True:
    LED16 = LED(16)
    LED15 = LED(15)
    LED14 = LED(14)
    LED13 = LED(13)
    
    print("even on, odd off")
    LED16.on()
    LED14.on()
    LED15.off()
    LED13.off()
    time.sleep(1)
<<<<<<< HEAD
    print("even off, odd on")
    LED16.off()
    LED14.off()
    LED15.on()
    LED13.on()
    time.sleep(1)
=======

    print("Even off, Odd on")
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(12 ,GPIO.LOW)
    GPIO.output(5 ,GPIO.HIGH)

    time.sleep(1)
>>>>>>> 9e2ce18b8d17bb262391c8ce84b121ac06be4dcd
