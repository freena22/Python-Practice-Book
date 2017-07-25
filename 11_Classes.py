
### Class

class Dog():
	name = 'luka'
	color = 'golden'
	def get_color(self):
		print(self.name)
		return self.color


obj = Dog()
obj.color = 'white'
obj.get_color()


# 'self' is the default parameter of the class
class Person:
	def say_hi(self):
		print('Hello, how are you?')
luka = Person()
luka.say_hi()  # -> Hello, Hou are you?

# _init_: initialization 

class Person:
    def __init__(self, name):
    	self.name = name
    def say_hi(self):
    	print('Hello, my name is', self.name)

Person('Lumi').say_hi()   # -> Hello, my name is Lumi.

# Class variables & Object variables
class Robot:
	# define a Robot with name
	population = 0 # a class variable for calculating the number of robots

	def __init__(self, name):
		# initialize the data
		self.name = name
		print('Initializing{})'.format(self.name))

		# When create one robot
		Robot.population += 1

	def die(self):
		print('{} is being destroyed!'.format(self.name))
		Robot.population -= 1

		if Robot.population == 0:
			print('{} was the last one'.format(self.name))
		else:
			print('There are still {:d} robots working'.format(Robot.population))

	def say_hi(self):
		print('Greeting, my masters call me {}.'.format(self.name))

# Robot.population -- class variable
# self.name -- object variable


droid1 = Robot('AA')
droid1.say_hi()
droid2 = Robot('BB')
droid2.say_hi()
print('\n****Robots can do some work here.****\n')

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
print('**********')
# Inheritance (Base Class and Derived Classes)
class Schoolmember:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print('Initialized Schoolmember:{}'.format(self.name))

	def tell(self):
		print('Name:{} Age:{}'.format(self.name, self.age))

class Teacher(Schoolmember):
	def __init__(self, name, age, salary):
		Schoolmember.__init__(self,name,age)
		self.salary = salary
		print('Initialized Teacher: {}'.format(self.name))

	def tell(self):
		Schoolmember.tell(self)
		print('Salary:{:d}'.format(self.salary))

class Student(Schoolmember):
	def __init__(self,name,age,marks):
		Schoolmember.__init__(self,name,age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))
	def tell(self):
		Schoolmember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))
t = Teacher('Mrs.Bao', 30,80000)
s = Student('Luka', 3, 99)

print('***********')
members = [t,s]
for member in members:
	member.tell() # call the tell() in subclass
# -> Name:Mrs.Bao Age:30
# -> Salary:80000
# -> Name:Luka Age:3
# -> Marks: "99"

