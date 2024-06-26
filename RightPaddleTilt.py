# Imports go at the top
from microbit import *
import radio
import time

# Code in a 'while True:' loop repeats forever
radio.config(group=23, power=7);
radio.on()

score = 0;

display.show('B')

while True:
    tempMes = radio.receive()
    if (tempMes == 'reset'):
        break
        
while True:
    yMag = compass.get_y()
    print(yMag)
    if(yMag >= 1000 and yMag < 10000):
        radio.send('b1')
    if(yMag >= 10000 and yMag < 20000):
        radio.send('b2')
    if(yMag >= 20000 and yMag < 30000):
        radio.send('b3')
    if(yMag >= 30000):
        radio.send('b5')
    if(yMag <= -8000 and yMag > -15000):
        radio.send('b-1')
    if(yMag <= -15000 and yMag > -25000):
        radio.send('b-2')
    if(yMag <= -25000 and yMag > -35000):
        radio.send('b-3')
    if(yMag <= -35000):
        radio.send('b-5')
    time.sleep(0.08)
