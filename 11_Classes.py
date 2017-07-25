
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