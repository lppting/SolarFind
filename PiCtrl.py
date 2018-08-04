#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time


OPEN = 20
CLOSE = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(OPEN,GPIO.OUT)
GPIO.setup(CLOSE,GPIO.OUT)

def PiOpen(pin,OpenTime):
    GPIO.output(pin,True)
    time.sleep(OpenTime)
    GPIO.output(pin,False)
#    GPIO.cleanup()
def PiClose(pin,CloseTime):
    GPIO.output(pin,True)
    time.sleep(CloseTime)
    GPIO.output(pin,False)
#    GPIO.cleanup()    
def MainControl(ControlTime):
#    OPEN = 21
#    CLOSE = 20
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(OPEN,GPIO.OUT)
#    GPIO.setup(CLOSE,GPIO.OUT)
#    print OPEN
    T = ControlTime
    if T > 0:
        PiOpen(OPEN,T)
    if T < 0:
        PiClose(CLOSE,0-T)
#    GPIO.cleanup()

if __name__ == "__main__":
    MainControl(-18)    
    GPIO.cleanup()
