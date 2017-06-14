
# 1. Opening files open() function

f = open("test.txt", "r") # r as read 
f = open('/my_path/my_file.csv','r') 

# 2. Read files read() function

f = open("crime_rates.csv", "r")
data = f.read()
f.close()   # close the file to free up resources 


# --- Combine to one line code 

vocabulary = open("dictionary.txt", "r").read()

# 3. Writing to a File

f = open('/my_path/my_file.txt','w')
f.write('Hello World!')
f.close()


# WITH : python allows to open a file, do operations and automatically close it afterwards using WITH
with open('/my_path/my_file.txt','r') as f:
    data = f.read()
# no need to call f.close()!
# it's a function -- Don't forget the ':' and indent

# for line in file: Python loop over the lines of a file 
# Use 'for line in file' to create a list of lines in the file.
# But each line still has its newline character attached, remove this using .strip()
camelot_lines = []
with open('camelot.txt') as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)
# Out: ['We're the knights of the round table','We dance whenever we're able']



# 4. splitting: run a string object into a list of strings
sample = "john,plastic,joe"
split_list = sample.split("\n")         
print(split_list)  # output: ['john','plastic','joe']

# split('\n') function

#Convert the List of Strings to a List of Lists and float() the Strings
print(nested_list[0:5])
numerical_list = []
for line in nested_list:  #split('\n or ,') depend on what word to split
    name = line[0]
    number = float(line[1])
    new_list = [name,number]
    numerical_list.append(new_list)
print(numerical_list)

# split('\n') OR  split(',') OR split(' ')

# Practice
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list

    
 
 
# Filter the List   
# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []
for line in numerical_list:
    name = line[0]
#    population = line[1]
    if line[1] >= 1000:
        thousand_or_greater.append(name)
print(thousand_or_greater)

# ------- organize the dataset ----------
# 1.  a general way to organize the raw dataset example(dataquest - list operation)
f = open('la_weather.csv', 'r')
data = f.read()
rows = data.split('\n')       # cut into rows
weather_data = []
for row in rows:
    split_row = row.split(',')
    weather_data.append(split_row)     # split into lists of lists
    
# output: [['Day', 'Type of Weather'], ['1', 'Sunny'], ['2', 'Sunny'], ['3', 'Sunny']...]

# 2. Getting a Single Column From the Data (grouped the data by column)
numbers = [[1,2],[3,4],[5,6],[7,8]]
second_column = []
for item in numbers:
    second_column.append(item[1])
    
# 3. Removing the header ( first element)
new_one = one[1:366]  # cutoff the index 0 element


# CSV file V.S. Text file
# CSV: Each line (representing a row) in a CSV file is separated by the newline character (\n), and each value in a line is separated by the comma delimiter (,). 
# Text: consists of 1 line of text that separates each word with a single whitespace (" ")

# Convert Raw data to ready-to-use data format

f = open("crime_rates.csv", 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

# Step 1: open and read               # Return a string

data = open('xxx.csv','r').read()   

# Output: Day,Type of Weather
#         1,Sunny
#         2,Sunny
#         3,Sunny
#         4,Sunny
#         5,Sunny
#         6,Rain


# Step 2: split the data into rows -- split('\n')   # Return a list
rows = data.split('\n')
# Output: ['Day,Type of Weather', '1,Sunny', '2,Sunny', '3,Sunny',...]

# Step 3: loop each row and split each row into a list on ','    # Return a list of lits 
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
print(full_data)
# Output: [['Day', 'Type of Weather'], ['1', 'Sunny'], ['2', 'Sunny'],...]

# Step 4: get a single column -- delete the 1,2.3.....

weather = []
for w in full_data:
    value = w[1]
    weather.append(value)
print(weather)
# Output: ['Type of Weather', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Sunny', 'Rain', 'Sunny'...]

# Step 5: Removing the header
new_weather = weather[1:366]

# Step 6: make the function optional -- add the last True/False

# We want story_string cleaned, so we set the third parameter to `True`.
tokenized_story = tokenize(story_string, clean_chars, True)
# Since we didn't pass in a value for the third parameter, `clean` will be set to `False` by default.
tokenized_vocabulary = tokenize(vocabulary, clean_chars)