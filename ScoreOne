# Imports go at the top
from microbit import *
import radio

# Code in a 'while True:' loop repeats forever
radio.config(group=23, power=7);
radio.on()

score = 0;

display.show('T')

while True:
    tempMes = radio.receive()
    if (tempMes == 'reset'):
        break
        
while True:
    if(int(score) < 10):
        display.show(int(score), wait=False)
    else:
        display.show(int(score)%10, wait=False)
    message = radio.receive()
    if message:
        if(message != 'reset' and message[0] == 'x'):
            score = message[message.index('c')+1: message.index('d')]   
 
