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

#Print grid
def repeat(string,appearance):
    print(string*appearance,end = '');

def block(string1,string2,string1Appearance,string2Appearance):
    repeat(string1,string1Appearance);
    repeat(string2,string2Appearance);
    
def dualBlock(string1,string2,string1Appearance,string2Appearance):
    block(string1,string2,string1Appearance,string2Appearance);
    block(string1,string2,string1Appearance,string2Appearance);

def display2x2():
    dualBlock('+','-',1,4);
    repeat('+',1);
    print();
    dualBlock('|',' ',1,4);
    repeat('|',1);
    print();
    dualBlock('|',' ',1,4);
    repeat('|',1);
    print();
    dualBlock('+','-',1,4);
    repeat('+',1);
    print();
    dualBlock('|',' ',1,4);
    repeat('|',1);
    print();
    dualBlock('|',' ',1,4);
    repeat('|',1);
    print();
    dualBlock('+','-',1,4);
    repeat('+',1);
    
print('\nDisplaying 2x2 grid')
display2x2();


def display4x4():
    dualBlock('+','-',1,4);
    dualBlock('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    dualBlock('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    dualBlock('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    dualBlock('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    dualBlock('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    dualBlock('+','-',1,4);
    repeat('+', 1);
    
print('\n\nDisplaying 4x4 grid')
display4x4();

def display2x3():
    dualBlock('+','-',1,4);
    block('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    block('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    block('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    block('+','-',1,4);
    repeat('+', 1);
    print();
    dualBlock('|',' ',1,4);
    block('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('|',' ',1,4);
    block('|',' ',1,4);
    repeat('|', 1);
    print();
    dualBlock('+','-',1,4);
    block('+','-',1,4);
    repeat('+', 1);

print('\n\nDisplaying 2x3 grid')
display2x3();

print('\n\nThink Python - Chapter 3 Programming - Completed!');