# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(group=23, power=7)
# Code in a 'while True:' loop repeats forever
while True:
    display.scroll('TX')
    if(button_a.is_pressed()):
        radio.send('A')
    elif(button_b.is_pressed()):
        radio.send('B')
    else:
        radio.send('')
    
