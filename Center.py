# Imports go at the top
from microbit import *
import radio
radio.config(group=23)
radio.on()
xMin = 5
xMax = 9
yMin = 0
yMax = 4
xMes = '0'
yMes = '0'
xAdjust = 5
yAdjust = 4
xPrev = 0
yPrev = 0
oldMes = ''
display.show('2')
while True:
    display.show('2')
    tempMes = radio.receive()
    if(tempMes == 'reset'):
        display.clear()
        break
    
while True:
    message = radio.receive()
    if(message == 'reset'):
        display.clear()
    elif(message):
        if(message != oldMes):
            display.clear()
            oldMes = message
        if(message[0] == 'x'):
            xMes = message[message.index('x')+1:message.index('y')]
            yMes = message[message.index('y')+1:message.index('a')]
            pongPos = message[message.index('a')+1:message.index('b')]
    
    if(int(xMes)>=xMin and int(xMes)<=xMax and int(yMes)>=yMin and int(yMes)<=yMax):
        display.set_pixel(xPrev, yPrev, 0)
        display.set_pixel(int(xMes)-xAdjust,yAdjust-int(yMes),9)
        xPrev = int(xMes)-xAdjust
        yPrev = yAdjust-int(yMes)
    
       