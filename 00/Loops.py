# while loops will continue until the condition becomes False.
index = 0
while index < 5:
	print(index)
	index += 1

# example: enter the correct password
	# password = input("Enter the password: ")
	# while password != "codingrules":
	# 	password = input("Wrong password. Try again: ")

	# print("Welcome Aboard!")

while True:
	password = input("Enter the password: ")

	if password == "codingrules":
		break # break exits the loop once the condition is met.

print("Welcome Aboard!")

# iterate, skips even numbers and prints the odd numbers.
x = 0
while x < 10:
 	x +=1 
 	if x % 2 ==0: # an even number
 		continue
 	print(x)

# iterate inside the following numbers list.
numbers = [2, 64, 34, 24, 86, 23]
# using while loop to iterate throught the list and multiplies each item by 2.
r = 0
while r < len(numbers):
 	print(numbers[r] * 2) # using the index r to get the elements inside the list.
 	r += 1

# using for loop to iterate throught the list and multiplies each item by 2.
for num in numbers:
	print(num * 2)
