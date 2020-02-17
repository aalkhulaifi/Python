'''
'''
from datetime import date
class Employee:
	def __init__(self, name, age, salary, employment_year):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_year = employment_year

	def get_working_years(self):
		current_year = date.today().year
		working_years = current_year - int(self.employment_year)
		return working_years
		# return date.today().year - self.employment_year

	def __str__(self):
		return f"Name: {self.name}, Age:{self.age}, Salary:{self.salary}, Working Years: {self.get_working_years()}"
			
class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus):
		super().__init__(name, age, salary, employment_year)
		self.bonus = bonus

	def get_bounus(self):
		return float(self.bonus) * float(self.salary)

	def __str__(self):
		return f"Name: {self.name}, Age:{self.age}, Salary:{self.salary}, Working Years{self.get_working_years()}, Bounus: {self.get_bounus()}"

employees_list = []
managers_list = []

print("Welcome to HR Pro 2020")
print("Options:")
print("\t1. Show Employees")
print("\t2. Show Managers")
print("\t3. Add An Employee")
print("\t4.Add A Manager")
print("\t5.Exit")
print("\t6. Go crazy")
print()
choice = int(input("What would you like to do:"))


while choice != 5:
	if choice == 1:
		for x in employees_list:
			print(x)
	elif choice == 2:
		for y in managers_list:
			print(y)
	elif choice == 3:
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_year = input("Employment Year: ")
		employee_obj = Employee(name , age, salary, employment_year)
		employees_list.append(employee_obj)

	elif choice == 4:
		name = input("Name: ")
		age = input("Age: ")
		salary = input("Salary: ")
		employment_year = input("Employment Year: ")
		bonus = input("Bounus Percentage:")
		manager_obj = Manager(name , age, salary, employment_year, bonus)
		managers_list.append(manager_obj)
	print("Welcome to HR Pro 2020")
	print("Options:")
	print("\t1. Show Employees")
	print("\t2. Show Managers")
	print("\t3. Add An Employee")
	print("\t4.Add A Manager")
	print("\t5.Exit")
	print("\t6. Go crazy")
	print()
	choice = int(input("What would you like to do:"))




