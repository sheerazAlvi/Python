'''
Created on Nov 8, 2018

@author: hp
'''

def polyline(t,repeat,length,angle):
    for i in range(repeat):
        t.fd(length)
        t.lt(angle)
        

def move(t,xAxis,yAxis):
    t.ht()
    t.pu()
    t.setpos(xAxis,yAxis)
    t.pd()