'''
Lists: is a series of elments that have a specific order. 
''' 
colors = ["Blue", "Red", "Cyan", "Violet"]

print(colors) #prints the entire list
print(colors[0]) #prints the first element in the list

#  Use the .append() method to add elements to the list

colors.append("Green")
# print(colors[4])

print(len(colors)) # The len() buitin function will return the length on the list once the list is passed as a parameter.

# Dictionaries: key , value pairs. to group different data to a single real life thing.

person = {
	"name" : "Fuse",
	"age" : 25,
} 

print(person["name"]) # prints the value "Fuse" using the key "name"

person["favorite drink"] = "lemonade" # to add to the list

print(person) # to display the entire dictionary

# prints evey the key in person dictionary (one way to loop through the dictionary)
for key in person: 
	print(f"This person's {key} is {person[key]}")

# prints evey the key and value in person dictionary (second way to loop through the dictionary)
for key, value in person.items():
	print(f"This person's {key} is {value}")
