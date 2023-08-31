from machine import Pin
led = Pin("LED", Pin.OUT)

def turnLEDOff():
  led.off()

def turnLEDOn():
  led.on()