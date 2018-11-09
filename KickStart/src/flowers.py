'''
Created on Nov 7, 2018

@author: hp
'''

import turtle
import math
from shared import polyline,move
        
def arc(t,radius,angle):
    arc_length = 2 * math.pi * radius * (angle / 360)
    repeat = int(arc_length) + 1
    step_length = arc_length / repeat
    step_angle = angle / repeat
    polyline(t, repeat, step_length, step_angle)

def circle(t,radius):
    angle = 360
    arc(t,radius,angle)

def leaf(t,radius,angle):
    for i in range(2):
        arc(t,radius,angle)
        t.lt(180-angle)

def flower(t,repeat,radius,angle):
    for i in range(repeat):
        leaf(t,radius,angle)
        t.lt(360/repeat)


t = turtle.Turtle()
move(t,0,-150)
flower(t,7,100,60)

move(t,-150,150)
flower(t,10,80,75)

move(t,150,150)
flower(t,20,300,18)
turtle.mainloop()