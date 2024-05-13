# Imports go at the top
from microbit import *
import radio

radio.on()
radio.config(group=23, power=7)
# Code in a 'while True:' loop repeats forever
while True:
    message = radio.receive()
    if message:
        display.scroll(message)
    else:
        display.scroll('RX')

