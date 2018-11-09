'''
Created on Nov 8, 2018

@author: hp
'''

import turtle
from shared import polyline

def polygon(t,repeat,length):
    step_angle = 360 / repeat
    step_length = int(length)
    polyline(t, repeat, step_length, step_angle)

t = turtle.Turtle()
polygon(t, 3, 100)
turtle.mainloop()    
