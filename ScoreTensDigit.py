# Imports go at the top
from microbit import *
import radio
import time

# Code in a 'while True:' loop repeats forever
radio.config(group=23, power=7);
radio.on()

score = 0;

display.show('S')

while True:
    tempMes = radio.receive()
    if (tempMes == 'reset'):
        break
        
while True:
    if(int(score) == 0):
        display.show(0, wait=False)
    if(int(score) >= 10):
        display.show(int(score)/10, wait=False)
    message = radio.receive()
    if message:
        if(message != 'reset' and message[0] == 'x'):
            score = message[message.index('c')+1: message.index('d')]   
 
