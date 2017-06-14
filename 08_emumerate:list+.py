
# enumerate() function: iterate over multiple lists

animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]
viciousness = [1, 5, 10, 10, 1]

for i, animal in enumerate(animals):  # use the natural index 
    #print("Animal Index")  ## label
    print(i)
    #print("Animal") ## label
    print(animal)

print('--------------')

for i, animal in enumerate(animals):
    #print("Animal")
    print(animal)
    #print("Viciousness")
    print(viciousness[i]) # Use index variable i to index the viciousness list

    
# Use the enumerate() function to add columns to lists of lists

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, thing in enumerate(things):
    thing.append(trees[i])
print(things)

# list Comprehensions -- slelect the elements in list to form a new list
print('--------------')
animals = ["Dog", "Tiger", "SuperLion", "Cow", "Panda"]

animal_lengths = []
for animal in animals:                       # Option 1: tradition for loop
    animal_lengths.append(len(animal))


animal_lengths = [len(animal) for animal in animals]    # Option 2: easy methord
print(animal_lengths)

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [(i*2) for i in apple_prices]
apple_prices_lowered = [(i-100) for i in apple_prices]
print(apple_prices_lowered)
print(apple_prices_doubled)

# above is the easy way to select or make changes in iterating elements in list


values = [None, 10, 20, 30, None, 50]
checks = []
checks = [ x is not None and x > 30 for x in values]
print(checks)


# items() -- which allows us to iterate through keys and values at the same time

fruits = {
    "apple": 2,
    "orange": 5,
    "melon": 10
}

for fruit, rating in fruits.items():
    print(fruit)
    print(rating)
    
plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for plant, k in plant_types.items():
    print(plant)
    print(k)
    
name_counts = {'Jo Ann': 2, 'Lynn': 1, 'Stephanie': 2, 'Anne': 1, 'Enid': 1, 'Thelma': 1, 'Mary Jo': 1, 'Olympia': 1, 'Carolyn': 1, 'Cynthia': 1, 'Jennifer': 1, 'Jane': 1, 'Ellen': 1, 'Virginia': 1, 'Barbara': 1, 'Betty': 1}   
top_female_names = []
for name, k in name_counts.items():
    if k == 2:
        top_female_names.append(name)
print(top_female_names)