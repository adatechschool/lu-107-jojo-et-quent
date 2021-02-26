class Pet:
	def __init__(self, name, greeting = "Hello"):
		self.name = name
		self.greeting = greeting

	def say_hi(self):
		print(f"{self.greeting}, I'm {self.name}!")
	
	@classmethod
	def legs_count(cls):
		cls.legscount = 4
		print(f"I have {cls.legscount} legs.")
		

class Cat(Pet):
	def __init__(self, name):
		super().__init__(name, "Meow")

class Parrot(Pet):
	def __init__(self, name):
		super().__init__(name, "Squawk")

	def say_hi(self):
		print(f"{self.greeting}, my name is {self.name}!")

	@classmethod
	def legs_count(cls):
		cls.legscount = 2
		print(f"I have {cls.legscount} legs.")

my_pet = Pet("Gaston")
my_pet.say_hi()
my_pet.legs_count()
cat = Cat("Félix")
cat.say_hi()
cat.legs_count()
parrot = Parrot("Perroquet")
parrot.say_hi()
parrot.legs_count() 
