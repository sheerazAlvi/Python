'''
Created on Nov 5, 2018

@author: hp
'''
#To print right justfied
def right_justify(s):
    length = len(s);
    justify = ' ' * (70-length) + s;
    return justify;

print(right_justify('Text has been right justified\n'));

#To print string multiple time
def print_string(s):
    print(s);

def do_twice(f,s):
    f(s);
    f(s);
    
def do_four(f,s):
    do_twice(f,s);
    do_twice(f,s);
    
print('Printing string twice');
do_twice(print_string,'twice');
    
print('\nPrinting string four times')
do_four(print_string,'four times');

#To print grid 2x2
print('\nDisplaying 2x2 grid')
def single(s): 
    f = print(s,end = '');
    return(f);
    
def repeat(s):
    f = print(s*4,end = '');
    return(f);

def sides(a,b):
    single(a);
    repeat(b);
    single(a);
    repeat(b);
    single(a);

def middle(a,b):
    single(a);
    repeat(b);
    single(a);
    repeat(b);
    single(a);

sides('+','-');
print('');
middle('|',' ');