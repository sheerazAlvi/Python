'''
Created on Nov 5, 2018

@author: hp
'''
import math

# Volume of a sphere
radius = 5**3;
volume = (4/3)*math.pi*radius;
print('Volume of a sphere =', volume);

#total wholsesale cost
coverPrice = 24.95;
discountedPrice = coverPrice - (coverPrice*(40/100));
totalWholesaleCost = (discountedPrice+3)+((discountedPrice+0.75)*59);
print('\nTotal wholesale Cost =',totalWholesaleCost);

#Exercise
startTimeSecs = ((6*60)+52)*60;
easyPace = ((8*60)+15)*2;
tempo = ((7*60)+12)*3;
totalTimeSecs = startTimeSecs + easyPace + tempo;
totalTimeHours = (totalTimeSecs/60)/60;
hours = int(totalTimeHours);
minutesTemp = (totalTimeHours - hours)*60;
minutes = int(minutesTemp);
print('\nArrival at home =', hours,':',minutes,'AM');

print('\nThink Python - Chapter 2 Programming - Completed!')