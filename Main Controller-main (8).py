# Imports go at the top
from microbit import *
import radio
import random
import music

timing = 20
counter = 0;

xstart = 12
ystart = 12
astart = 10
bstart = 10

xpos = xstart
ypos = ystart
xvel = 1
yvel = -1

upperLim = 25
lowerLim = 0
rightLim = 25
leftLim = 0

apos = astart
bpos = bstart
ascore = 0
bscore = 0

alower = 0
aupper = 20
blower = 0
bupper = 20

radio.config(group=23, power=7)
radio.on()

# Code in a 'while True:' loop repeats forever
while True:
    display.show("Z", wait=False)
    if(ascore == 9 or bscore == 9):
        while(True):
            display.show(" ", wait=False)
            music.play(music.WAWAWAWAA)
            if(button_a.is_pressed()):
                break
    if(button_b.is_pressed()):
        while(button_b.is_pressed()):
            #wait
            print('paused')
        while(not button_b.is_pressed()):
            print('paused')
        while(button_b.is_pressed()):
            print('paused')
    if(button_a.is_pressed()):
        radio.send('reset')
        apos = astart
        bpos = bstart
        ascore = 0
        bscore = 0
        xpos = xstart
        ypos = ystart
    if(counter == timing):
        counter = 0
        
        if(xpos == leftLim):
            if(((ypos<apos) or (ypos > (apos+5)))):
                bscore = bscore + 1
                xpos = xstart
                ypos = ystart
                apos = astart
                bpos = bstart
                music.play(music.POWER_DOWN)
            else :
                ypos = ypos + random.randint(-1,1)
                xvel = -xvel
                music.play(music.BA_DING, wait=False)
        if(xpos == rightLim-1):
            if(((ypos<bpos) or (ypos > (bpos+5)))):
                ascore = ascore + 1
                xpos = xstart
                ypos = ystart
                apos = astart
                bpos = bstart
                music.play(music.POWER_DOWN)
            else:
                ypos = ypos + random.randint(-1,1)
                xvel = -xvel
                music.play(music.BA_DING, wait=False)

        xpos = xpos + xvel            
        
        ypos = ypos + yvel
        if(ypos <= lowerLim):
            yvel = random.randint(1,3)
        if(ypos >= upperLim):
            yvel = -random.randint(1,3)
    
    message = radio.receive()
    if message:
        if(message[0] == 'a'):
            apos = apos + int(message[1:])
        if(message[0] == 'b'):
            bpos = bpos + int(message[1:])
            
    if(apos < alower):
        apos = alower
    if(apos > aupper):
        apos = aupper
    if(bpos < blower):
        bpos = blower
    if(bpos > bupper):
        bpos = bupper
        
    output = 'x' + str(xpos) + 'y' + str(ypos) + 'a' + str(apos) + 'b' + str(bpos) + 'c' + str(ascore) + 'd' + str(bscore) + 'e'
    radio.send(output)
    print(output)
    print(str(xvel) + '' + str(yvel))
    counter = counter + 1