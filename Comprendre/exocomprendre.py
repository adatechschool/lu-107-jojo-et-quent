class Pet:
	def __init__(self, name, greeting = "Hello"):
		self.name = name
		self.greeting = greeting

	def say_hi(self):
		print(f"{self.greeting}, I'm {self.name}!")
	
	@classmethod
	def legs_count(cls):
		cls.legscount = 4
		pass # do nothing

class Cat(Pet):
	def __init__(self, name):
		super().__init__(name, "Meow")

class Parrot(Pet):
	def __init__(self, name):
		super().__init__(name, "Blabla")

	def say_hi(self):
		print(f"{self.greeting}, my name is {self.name}!")

my_pet = Pet("Gaston")
my_pet.say_hi()
cat = Cat("Félix")
cat.say_hi()
parrot = Parrot("Perroquet")
parrot.say_hi()
# print(Cat.legs_count())
# print(Parrot.legs_count())