
""" Summary

# list = []
# tuple = ()   -- no change， more safer
# dict = {}    -- key-value 
# set()        -- no order and no repeated elements

"""

### 1: List -- check/modify/delete/slice


number = [1,2,3,4,5]
family = ['dad','mom','luka','lumi']

print(family[2])  # Out：luka
print(family[-1]) # Out: lumi


# Index Errors
my_list = ['a','b','c','d','e']
print(my_list[4])  # Out：e
print(my_list[5])  # Out: IndexError: list index out of range

# Practice
def how_many_days(month_number):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month_number-1]
how_many_days(8)    # Out: 31

# Slicing 

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# Modify this line so it prints the last three elements of the list
print(eclipse_dates[7:]) 
# OR 
print(eclipse_dates[-3:])

# mutability

sample_list = ['Graham', 'John', 'Terry', 'Apple', 'Terry', 'Michael']
sample_list[3] = 'Eric'
print(sample_list)   # Out: ['Graham', 'John', 'Terry', 'Eric', 'Terry', 'Michael']

# Working with Lists
batch_sizes = [15, 6, 89, 34, 65, 35]
len(batch_sizes)     # Out: 6
max(batch_sizes)     # Out: 89
min(batch_sizes)     # Out: 6
sorted(batch_sizes)  # Out: [6, 15, 34, 35, 65, 89]
sorted(batch_sizes, reverse=True)  # Out: [89, 65, 35, 34, 15, 6]

# Joining lists

nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)
# Out: 
fore
aft
starboard
port

names = ["García", "O'Kelly", "Davis"]
print("-".join(names))
# Out: "García-O'Kelly-Davis"

# Appending to Lists

family.append('apple')  # append() function
print(family)

family.insert(0,'God')  # insert() function
print(family)

family.pop(0)           # pop() function to delete
print(family)

print(family[1:3])      # slicing the list

some = ['apple', [2,3,4], 'luka',66,77]  
print(len(some))        # list can include nested-lists
L = []                  # create a empty list
print(len(L))

# Practice 1: Returns a list of the three largest elements input_list 

def top_three(input_list):
    return sorted(input_list, reverse=True)[:3]

# Practice 2: Find Median in A List
def median(numbers):
    numbers.sort() 
    if len(numbers) % 2:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        # if the list has an even number of elements,
        # the median is the average of the middle two elements
        right_of_middle = len(numbers)//2 
        left_of_middle = right_of_middle - 1
        return (numbers[right_of_middle] + numbers[left_of_middle])/2


### 2. Set -- Removing Duplicates from Lists

def remove_duplicates(source):
    target = []
    # build a empty list first
    for element in source:
        if element not in target:
            target.append(element)

    return target


unique_animals = set(["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"])
print(unique_animals)   # Out: ["Dog", "Cat", "Hippo"]


### 3. Dictionary: A dictionary is like a list in that it has indexes. score{}
#  key-value storage -- easy to find the elements


# Populating a Dictionary
students = {}
students["Jerry"] = 60
students['Apple'] = 90

# Defining a Dictionary with Values

animals = {7:'raven', 8:'goose', 9:'duck'}   # 9 is the key and 'raven' is value 

times = {
    "morning": 9,
    "afternoon": 14,                         # 'morning' is key and 9 is value
    "evening": 19
}
   
print(animals[7])
print(times['morning'])

score = {'apple':99, 'luka':66,'lumi':88}
print(score['apple'])                       # check students' score

# Modify the Dictionary
students = {
    "Tom": 60,
    "Jim": 70
}
students["Ann"] = 85                       # add Ann: 85 to the dic 
students["Tom"] = 80                       # replace Tom's score to 80
students["Jim"] = students["Jim"] + 5      # add 5 to Jim's score

# Practice 1: catelogizeing the elements into subgroups
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for length in planet_names:
    if len(length) > 5:
        long_names.append(length)
    else: 
        short_names.append(length)
        
# Practice 2
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for item in pantry:
  if item in pantry_counts:
        pantry_counts[item] =  pantry_counts[item] + 1
  else: 
        pantry_counts[item] = 1
print(pantry_counts)


# What's in the Dictionary?

if 'mithril' in elements:
    print("That's a real element!")
else:
    print("There's no such element!")
# OR 
elements.get('dilithium')   # Out: None

# Iterating over Dicts and Sets: in an arbitrary order

colors = set(['Pthalo Blue', 'Indian Yellow', 'Sap Green'])
for color in colors:
    print(color)

""" Out 
Indian Yellow
Sap Green
Pthalo Blue
"""
# Practice 4

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))


# A Dictionary of Dictionaries

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print(elements['helium'])
# Out: {'number': 2, 'symbol': 'He', 'weight': 4.002602}
print(elements['helium']['weight'])
# Out: 4.002602


### 4: Tuple 
# list use [] v.s.Tuple use ()
# list can change(append(), pop()) but Tuple cannot: tuples are immutable!
print('Tuple -------------------')

some1 = ('apple', 'luka')
print(some1[1])

# Tupes can be used to assign multiple variables in a compact way:
dimension = 52, 40, 100    # the parentheses are optional when making tuples 
length, width, height = dimensions
print('The dimensions are {}x{}x{}'.format(length, width, height))
# Out: The dimensions are 52x40x100

# Returning Tuples: a common use for tuples is to return multiple values from a function
def first_and_last(sequence):
    '''returns the first and last elements of a sequence'''
    return sequence[0], sequence[-1]
first_and_last('spam','egg','sausage','spam')
# Out: ('spam','spam')
start, end = first_and_last(['spam','egg','sausage','spam'])
print(start)   # Out: spam
print(end)     # Out: spam

# practice
def hours2days(input_hours):
    days = input_hours//24
    hours = input_hours%24
    return days, hours
hours2days(24)    # out: (1,0)
hours2days(25)    # Out: (1,1)
