'''
Created on Nov 7, 2018

@author: hp
'''

import turtle
import math

def polyline(t,repeat,length,angle):
    for i in range(repeat):
        t.fd(length)
        t.lt(angle)
    
def polygon(t,repeat,length):
    step_angle = 360 / repeat
    step_length = int(length) + 15
    polyline(t, repeat, step_length, step_angle)
    
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

def flower():

t = turtle.Turtle()
#circle(t,50)
#polygon(t, 4, 100)
#arc(t,200,50)
leaf(t,200,35)
t.lt(90)
leaf(t,200,35)
#polyline(t, 10, 50, 20)
turtle.mainloop()
