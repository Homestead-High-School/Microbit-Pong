# Imports go at the top
from microbit import *
import radio

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
    display.show(score, wait=False)
    message = radio.receive()
    if message:
        if(message != 'reset' and message[0] == 'x'):
            score = message[message.index('d')+1: message.index('e')]
    if(button_a.was_pressed()):
        radio.send('b1')
    if(button_b.was_pressed()):
        radio.send('b-1')
