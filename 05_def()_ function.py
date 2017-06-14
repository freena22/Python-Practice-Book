

# Create a self-defined interval clock
# Step 1: import the functions (webbrowser/time) and set the clock

import webbrowser
import time
time.sleep(60)
webbrowser.open('https://www.youtube.com/watch?v=uCMdn61JMd4')

#Step 2: Adding a loop (2 hours interval)

import webbrowser
import time
total_breaks = 3
break_count = 0
print ('This program started on ' + time.ctime())
while (break_count , total_breaks):
  time.sleep(60)
  webbrowser.open('https://www.youtube.com/watch?v=uCMdn61JMd4')
  break_count = break_count +1 
  
# Procedural abstraction (not built-in operator, you define!)
# def <name> (<inputs>,<input>,...):  input == ()/(page)/(a,b,c)
#     <block>
# e.g. find('au',3)

# one variable

def rest_of_string(s):           # s = 'audacity'
  return s[1:]
print(rest_of_string('audacity')) # output = 'udacity'

def my_abs(x):
  if x >= 0:
    return x 
  else:
    return -x

# two variables    
def sumadd(a,b):
	a = a + b
	return a 
print(sumadd(1,101))  # output = 102

def sum3(a,b,c):
  return a+b+c
print(sum3(1,2,3))    # output 6

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
print(enroll('Apple','F'))

# Set default variables behide
def enroll2(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
print(enroll2('Apple','F'))
print(enroll2('Bao','M', 30, 'Chifeng'))