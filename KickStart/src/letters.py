'''
Created on Nov 9, 2018

@author: hp
'''

import turtle
from shared import move

def draw_a():
    t.lt(60)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.bk(50)
    t.lt(60)
    t.fd(50)
    
t = turtle.Turtle()
#move(t,0,0)
draw_a()
turtle.mainloop()