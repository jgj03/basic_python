#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

a = 1
print(a)
################ MATH MODULES
import math
b = math.pi*(math.cos(45))
print(a)

c = math.cos(2 * math.pi)
print(c)

from math import * #Import the whole module into the current namespace 
d=cos( 2*pi)
print(d)

print(dir(math))
help(math.cos)

################ VARIABLES
e = 1
type(e)
f = 1.0
type(f)

################ OPERATORS
[1+1, 1-1, 1*1, 1/1]
3/2
3//2
3.0//2.0
2**2
True and False
True or False
not True
[1>2, 3>2]
2>1, 2<1, 2>2, 2<2, 2>=2, 2<=2
[1,2] == [2,1]
[1,2] == [1,2]

################ STRINGS
g = "Hello Python"
type(g)
len(g) 
g1=g.replace('Python','World')
print(g1)
g[:]
g[0]
g[:2]
g[2:]
g[::2] # gap os 2
g[-2::] # Last 2
g[::-1] # Reverse
g[::-2] # Reverse gap of 2

print("str1", "str2", "str3")
print("value = %d" % 1.0) # C-style formatting
print("value = %f" % 1.0) # C-style formatting
s3 = 'value1 = {0}, value2 = {1}'.format(3.1415, 1.5) # a formatting way
print(s3)

################ LISTS
h=[1,2,3,4]
print(h)
print(h[1:3])
print(h[2:4])
h[0]
range(0,10,2)
start=0
stop=20
step=5
range(start,stop,step)
i = [1, 'a', 1.0, 1-1j] # no need to be of the same type
print(i)
# append
j=[]
j.append('A')
j.append(2)
j.append('B')
j.append(3)
print(j)
# insert
j.insert(0, "i")
j.insert(1, "n")
j.insert(2, "s")
j.insert(3, "e")
j.insert(4, "r")
j.insert(5, "t")
print(j)
# remove
j.remove('A')
# delete
del(j[6])
del(j[7])
print(j)

################ TUPLES
point = (1, 2)
print(point, type(point))
# Unpacking
x,y=point
print('x:',x)
print('y:',y)

################ DICTIONARIES
params={'p1': 1,'p2': 2, 'p3': 3}
print(params)
print(type(params))
params['p4']=4 # adda new entry
print(params)
params['p1']='one' # edit existing entry
print(params)
print("p1 = " + str(params["p1"]))
print("p2 = " + str(params["p2"]))
print("p3 = " + str(params["p3"]))
print("p4 = " + str(params["p4"]))

################ CONTROL FLOW
statement1 = False
statement2 = False

if statement1:
    print('statement1 is True')
elif statement2:
    print('statement2 is True')
else:
    print('statement1 & statement2 is True')
 
################ LOOPS
for x in range(4):
    print(x)

l=['Python','is','a','programming','language']
for i in l:
    print(i)
print(i)

params={'p1': 1,'p2': 2, 'p3': 3}
for key,value in params.items(): # dont orget end braces()
    print(key+' = '+str(value))

for idx,x in enumerate(range(-3,3)):
    print(idx,':',x)

l1=[x**2 for x in range(0,3)]
print(l1)

i=0
while i<5:
    print(i)
    i=i+1
print('Finished')

################ FUNCTIONS
def string_length(s):
    """
    Prints the length of the string
    """
    print(s + " has " + str(len(s)) + " characters")
string_length("word")
help(string_length)

def square(x):
    return x**2
square(2)
square(4)

def powers(x):
    return x**2, x**3, x**4
powers(2)
x1,x2,x3=powers(5)
print(x3)

import numpy as np
np.power(2,2)
np.power(2,5)

sqr=lambda x : x**2
sqr(3)

#lambda functions
fn=map(lambda x: x**3, range(-2,3))
print(fn)
map(lambda x: x**2, range(-2,3))
# convert iterator to list
list(map(lambda x: x**2, range(-3,4)))

################ CLASSES
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def translate(self,dx,dy):
        self.x += dx
        self.y += dy
    def __str__(self):
        return ("Point: [%f,%f]" %(self.x,self.y))

p1=Point(1,1)
print(p1)
p2=p1.translate(.1,.1)
print(p1)
print(p2)

################ EXCEPTIONS
try:
    print("Test")
except:
    print(str(e))
#while printing undefined variable test:
try:
    print(test)
except Exception as e:
    print("An exception:"+str(e))
#another way of defining
try:
    print(test)
except Exception as e:
    print("An exception:",str(e))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
################ SOME PYTHON MAGICS #used in interactiv environemnts like jupyter
help
help(np) 
quit

%magic # help module for magic commands
%lsmagic # list of all available magic commands
%timeit? # bring up the help module for a specific command

x = 5
x?

# run a python script from within the notebook
%run scripts/hello.py
%debug # debug a statement either in-line or after the fact

# time the execution of a statement
import numpy as np
%timeit np.linalg.eigvals(np.random.rand(100,100))

# additional magic can be loaded using load_ext
%load_ext Cython

# list all environment variables or specific variables
%env SYSTEMROOT

# print the cache of previously executed commands
%history

# set matplotlib to inline or interactive (qt) mode
%matplotlib inline

# print the call signature for any object
import urllib
%pdef urllib.urlopen
# print the docstring for a class/callable object
%pdoc urllib

%who # print all interactive variables
%whos # same as who but more information

# example using cProfile
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 1

def fprime(x):
    return 3*x**2

# reset the namespace 
%reset # press yes if needed
%reset?
