
# 1. for loop - interate each element in order 


cities = ['Toledo','Boston','Worcester','Sunnyvle','San Jose']
for city in cities:
  print(city)


cities_in_school = cities[0:3]
for earlycity in cities_in_school:
  print(earlycity)
  
Total = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
  Total = Total + x     # sum(1-10): using for loop
print(Total)

# Define a function, list_sum, takes a list as argument and returns the sum of the elements in the list.
def list_sum(input_list):
	sum = 0
	for element in input_list:
		sum += element
	return sum

total1 = 0 
for x in range(101):    # range() function: create the list
  total1 = total1 + x   # sum(0-100)  # range(5) = [0,1,2,3,4,5]
print(total1)


# 2. while loop


A = 0                   # set the start value (0 or empty list)
n = 99                  # sum of all the odds in 100 
while n > 0:
  A = A + n 
  n = n -2
  
print(A) 


# Difference between 'while' and 'if': while - 0,1,2,...times
#                                      if - 0 or 1 times

i = 22
while i > 10:
	print(i)
	i = i -1  # without this, will be a infinite loop

# combine def and while loop -- as example not running 
def print_numbers(n):
	x = 0
	while x < n:
		x = x + 1
		print(x)
print_numbers(5)  # output: 1 2 3 4 5

# loop with the break: break out in the middle of the loop 

def print_numbers(n):
	x = 1
	while True:
		if x > n:
			break
		x = x +1
		print(x)
print_numbers(10)  # ouput: 2,3,4,5,6,7,8,9,10,11

# ???Difference between for-loop and while-loop???
# for-loop: can only iterate (loop) "over" collections of things. 
# while-loop can do any kind of iteration (looping) you want. However, while-loops are harder to get right and you normally can get many things done with for-loops.

# Practice: Define a check_answers function 

def check_answers(my_answers,answers):
    #1 variable names are not easy to tell apart
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    #2 Code will only work if there are exactly five answers
    results= [None, None, None, None, None]
    #3 Repeated code would be better as a separate function
    if my_answers[0] == answers[0]:
        results[0] = True
    elif my_answers[0] != answers[0]:
        results[0] = False
    #4 if and elif could be clearer with if and else
    if my_answers[1] == answers[1]:
        results[1] = True
    elif my_answers[1] != answers[0]:
        results[1] = False
    if my_answers[2] == answers[2]:
        results[2] = True
    elif my_answers[2] != answers[2]:
        results[2] = False
    if my_answers[3] == answers[3]:
        results[3] = True
    elif my_answers[3] != answers[3]:
        results[3] = False
    if my_answers[4] == answers[4]:
        results[4] = True
    elif my_answers[4] != answers[4]:
        results[4] = False
    #6 this function does several things in one long block
    count_correct = 0
    count_incorrect = 0
    for result in results:
    #7 The code counts both correct and incorrect answers.
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
    #8 The pass rate has been hard-coded into the function
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."



# IF Statement

# Nesting IF Statement

family = ['apple','mom','dad','luka','lumi']
if family[0] == 'apple':
  if family[1] == 'mom':          # 1st True then 2ed True ... all True then print
    if family[-1] != 'lulu':
      family = ['Good','day','sunny','cool','lucy']
print(family)

# Combine IF and For while

Result = False
for name in family:
  if name == 'lucy':              # iteration all the elements and judge whether belongs to 
    Result = True
print(Result)

Alist = [1,2,3,4,5]
Blist = [1,2]
for number in Alist:
  if number >= 3:
    Blist.append(number)
print(Blist)

print('-------------')
# find the biggest one 
age = [2,3,7,899,55,66]
biggest = age[0]

for x in age:
    if x > biggest:               #  use the PRINT in different locations to test
        biggest = x 
print(biggest)


# In statement : a easy way to find x in a lsit or not

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals 
print(cat_found)                               # output: True
space_found = 'space_monster' in animals
print(space_found)                             # output: False

# Practice to use def() and IF statement

def absolute(x):
  if x < 0:
     x = -x
  return x

# Two ways to define bigger
def bigger(a,b):      #1
  if a > b:
    return a          # simple way
  else:
    return b

def bigger(a,b):      #2
  if a > b:
    r = a             # assign a new 'r', in some case needed 
  else:
    r = b
  return b

def is_friend(name):  #3
  return name[0] == 'D' or name[0] == 'S'  # name[0] == 'D' or 'S' is WRONG!
print('True') 

print(is_friend('Dana'))       # output: True
print(is_friend('Freena'))     # output: False 

def biggest(a,b,c):b           # Use the defined bigger function to simplize
  return bigger(bigger(a,b),c) # build-in max()
  

