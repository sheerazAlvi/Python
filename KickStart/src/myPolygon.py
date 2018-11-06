'''
Created on Nov 6, 2018

@author: hp
'''

import turtle

def polygon(input,Occurence,length):
    input = turtle.Turtle()
    angle = 360 / Occurence
    for i in range(Occurence):
        input.fd(length)
        input.lt(angle)
    turtle.mainloop()
    
polygon('alice',Occurence=3,length=10)
