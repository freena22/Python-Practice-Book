# 1. For Loop

bag = [12, 345, 678, 45, 34,56,77,88,99]
for item in bag:
	print(item)

i = 0
for item in bag:
	i = i + 1
	print(i) # -> 1,2,3,4,5,6,7,8,9
# 所以loop 只不过是一种循环方式，而非一定的输出。可以输出为i 但是借助于bag这个list的loop7次这个模式
for x in range(8):
	print(bag[x])
# 把bag里的所有元素打出来了

# 2. While Loop

x = 10
while x < 12:
	print('yeah')
	x = x + 1  # -> yeah yeah 
# while 是条件，条件若不中断（一直不满足） 就会一直循环执行下去

# 3. Conditionals

list_a = [1,2,3,4]
for i in list_a:
	print(i**2) # -> 1,4,9,16 

for i in list_a:
	if i == 2:
		print("yup it's two")
	elif i == 1:
		print('first one')
	else:
		print(i)
# -> first one -- yup it's two -- 3,4

list_d = ['luka','apple',22,44,66,'lumi']
list_e = []
for i in list_d:
	if isinstance(i,int):
		list_e.append(i)
print(list_e)
# -> [22,44,66]
# 筛选出list里面的数字然后放到新list里去

x = 0
list_d = [1,'luka','apple',66,'lumi',9]
list_e = []
for item in list_d:
	if isinstance(item, int):
		print(item) # -> 1,66,9
		list_e.append(item)
		list_d.pop(x)
	x += 1

print(list_d) # -> ['luka','apple','lumi']
print(list_e) # -> [1,66,9]

# 4. Functions

items = ['mic', 'phone', 22, 344, 56.78, 34.7, 'bag','cute',23]
str_item = []
num_item = []

for i in items:
	if isinstance(i,float) or isinstance(i,int):
		num_item.append(i)
	elif isinstance(i,str):
		str_item.append(i)
	else:
		pass

print('-----')

def parse_lists(any_list):
	str_item = []
	num_item = []
	for i in any_list:
		if isinstance(i,float) or isinstance(i,int):
			num_item.append(i)
		elif isinstance(i,str):
			str_item.append(i)
		else:
			pass
	return str_item, num_item

print(parse_lists(items))

def my_sum(any_list):
	total = 0
	for i in any_list:
		if isinstance(i,float) or isinstance(i,int):
			total += i
	return total
# 弥补sum()不能相加str & num的error问题
print(my_sum(items))

def my_sum_and_my_count(any_list):
	total = 0
	count = 0
	for i in any_list:
		total = my_sum(any_list)  # call the my_sum()
		count += 1
	return total, count
print(my_sum_and_my_count(items))

# 5. Advanced Strings

# String Substitue -- see more on 30_days_cheet_sheet

name_list = ['luka','lumi','apple','lily','gb']
for i in name_list:
	'My name is {name}'.format(name=i)
# -> all the names in this format
"This is a argument {0} {1} {0} {1}".format('luka','apple')
# -> This is a argument luka apple luka apple

'Hi there %s! Thanks.' %('Luka')
# -> Hi there Luka! Thanks!

import datetime
datetime.datetime.now()
# check more on cheat sheet

# 6. String Formatting Function

print('+++++++++++++')
default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""

def make_message(names, amounts):
	i = 0
	today = datetime.datetime.today() 
	text = '{today.month}/{today.day}/{today.year}'.format(today=today)
	for name in names:
		new_amount = "%.2f"%(amounts[i]) # loop the amounts
		name = name[0].upper() + name[1:].lower() # change the first one to Capital
		new_msg = unf_message.format(
			name = name,
			date = text,
			total = new_amount
		)
		i += 1
		print(new_msg)
make_message(default_names, default_amounts)









