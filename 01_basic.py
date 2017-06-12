

# 1. Arthmetic Operation
print(2+3)
print(3*2)
print(3**2)  # Out: 9 **: raise one number to the power of another, not ^
print(9%2)   # Out: 1 get the remainder
print(15//4) # Out: 3 rounds the answer down to an integer


# 2: Assignment Statement = 

aa = 'lala'              # assign value to variable
print(aa)

family = ['mom', 'dad', 'luka', 'lumi'] 
print(family)            # assign values to list 

number = [1,2,3,4]
print(number)

# Using multiple assignment
savings, salary = 400, 329.5 

# 3. Reassignment Operators
total += 100   # total = total + 100
total -= 100
total *= 100
total /= 2 


# 4: Data Type and Converting Types

print(type(family))    # type() function
t = (1,)
print(type(t))   # Out: 'tuple'

china_rounded = 123
int_to_str = str(china_rounded)
str_to_int = int (int_to_str)  # str() & int() functions
print(type(int_to_str))
print(type(str_to_int))

print('luka'*3)  # Out: lukalukaluka


# 5. Strings

# use the + to concatenate the two strings together to print
a = 'Philip'
b = 'Charlie'
print(a + 'and' + b)   # Out: Philip and Charlie

# len function to find the length of strings not numbers
print(len(a))

# String Methods:
'one fish, two fish, red fish'.count('fish')
# Out: 4 
'one fish, two fish, red fish'.islower() 
# Out: True


print('luka is night\n luka is good'.split('\n'))
# Out: ['luka is night', ' luka is good']

# String Formatting: use to construct strings by inserting values into template strings.
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)
print(log_message)
# Out: IP address 208.94.117.90 accessed /bears/koala at 16:20

