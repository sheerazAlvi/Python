'''
Created on Nov 8, 2018

@author: hp
'''

import turtle
import cmath
import math
from shared import move

def isosceles(t,twoSideslength,firstAngle):
    #unknown side = sqrt (a^2 + b^2 - 2abcos(angle)) -> law of cosine
    thirdSide = round(math.sqrt((twoSideslength**2) + (twoSideslength**2) - (2*twoSideslength*twoSideslength*math.cos(math.radians(firstAngle)))),2)
    #second angle = sin^-1(knownLength * sin(angle) / knownlength) -> law of sine
    secondAngle = round(math.degrees(math.asin((twoSideslength * math.sin(math.radians(firstAngle)))/thirdSide)),2)
    #angle of triangle = 180
    thirdAngle = 180 - firstAngle - secondAngle
    #Drawing  
    t.fd(twoSideslength)
    t.lt(180-firstAngle)
    t.fd(twoSideslength)
    t.lt(180-secondAngle)
    t.fd(thirdSide)
    t.pu()
    t.lt(180)
    t.fd(thirdSide)
    t.rt(180-secondAngle)
    t.pd()
    
def inscribedPie(t,repeat, length):
    angle = 360/repeat
    for i in range(repeat):
        isosceles(t, length, angle)

t = turtle.Turtle()
move(t,0,-100)
inscribedPie(t,5,75)
move(t,-200,100)
inscribedPie(t,6,75)
move(t,150,100)
inscribedPie(t,7,75)
turtle.mainloop()