# Imports go at the top
from microbit import *
import radio
radio.config(group=23)
radio.on()
xMin = 0
xMax = 4
yMin = 5
yMax = 9
xMes = '0'
yMes = '0'
xAdjust = 0
yAdjust = 9
xPrev = 0
yPrev = 0
pongPos = '0'
oldMes = ''
display.show('6')
while True:
    display.show('6')
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
    
    if(int(pongPos)>=yMin and int(pongPos)<=yMax):

        pos = int(pongPos)
        while(pos <= yMax):
            display.set_pixel(0,yAdjust-pos, 9)
            pos+=1
    elif (int(pongPos)+5>=yMin and int(pongPos)+5<=yMax):
        pos = int(pongPos)+4
        while(pos >= yMin):
            display.set_pixel(0,yAdjust-pos, 9)
            pos-=1
    
    if(int(xMes)>=xMin and int(xMes)<=xMax and int(yMes)>=yMin and int(yMes)<=yMax):
        display.set_pixel(xPrev, yPrev, 0)
        display.set_pixel(int(xMes)-xAdjust,yAdjust-int(yMes),9)
        xPrev = int(xMes)-xAdjust
        yPrev = yAdjust-int(yMes)
    
       