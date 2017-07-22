

class Dog():
	name = 'luka'
	color = 'golden'
	def get_color(self):
		print(self.name)
		return self.color


obj = Dog()
obj.color = 'white'
obj.get_color()
