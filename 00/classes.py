# The variables inside the classes is called attributes.
# Functions inside clases is called methods. Methods with double under scores called dunder methods and they are reserved by Python.
# Every method inside a class, has to have a parameter called 'self' as the first parameter.
class Person:
	def __init__(self, name_parameter, age_parameter):
		self.name = name_parameter
		self.age = age_parameter

	def greeting(self):
		print(f"Hello, my name is {self.name}, and I am {self.age} years old.")

	def __str__(self):
		return self.name 


# Generate a person
sam = Person("Sam", 34)

#  Calling a method inside of a class
sam.greeting()

# User inputs their name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

user = Person(name, age)
user.greeting()

class Car:
	def __init__(self, model, color):
		self.model = model
		self.color = color
		self.speed = 0

	def accelerate(self, value):
		self.speed += value 

maxima = Car("Maxima", "Maroon")
accord = Car("Accord", "Red")

print(f"Maxima is going {maxima.speed} km/h")
maxima.accelerate(5)
print(f"Maxima is going {maxima.speed} km/h")

print(f"Accord is going {accord.speed} km/h")
accord.accelerate(3)
print(f"Accord is going {accord.speed} km/h")

# inheritance. The follwing class "Student" will inherit everything from "Person" class.
#super() refers to the parent class "Person".
class Student(Person):
	def __init__(self, name, age, subjects):
		super().__init__(name, age)
		self.subjects = subjects

hanan = Student("Hanan", 25, ["Art", "Science"])
jaber = Student("Jaber", 26, ["Health", "Science"])

for subject in hanan.subjects:
	print(f"Hanan is interested in {subject} ")

for subject in hanan.subjects:
	print(f"Jaber is passionate about {subject} ")

hanan.greeting()
jaber.greeting()

students = {
	"male": [jaber],
	"female": [hanan]
}

for male_student in students["male"]:
	print(f"One of our male students is: {male_student.name}")

for female_student in students["female"]:
	print(f"One of our female students is: {female_student.name}")
