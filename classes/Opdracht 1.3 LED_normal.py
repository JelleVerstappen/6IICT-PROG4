import RPi.GPIO as GPIO # Only works on Raspberry Pi
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(26,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)


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
    print("even off, odd on")
    LED16.off()
    LED14.off()
    LED15.on()
    LED13.on()
    time.sleep(1)