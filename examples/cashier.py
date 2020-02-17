'''
'''
item_list = []

item_name = input("Item (enter 'done' when you're done): ")

while item_name != "done":
	price = float(input("Price: "))
	quantity = int(input("Quantity: "))
	item_dictionary = {
		"name": item_name,
		"price": price,
		"quantity": quantity
	}

	item_list.append(item_dictionary)

	item_name = input("Item (enter 'done' when you're done): ")

print()
print("----------")
print("Receipt")
print("----------")

# print the individual items
total = 0
for item in item_list:
	print(f"{item['quantity']} {item['name']} {item['price'] * item['quantity']} KWD")
	total += item['price'] * item['quantity']

# # Calculate the price
# total = 0
# for item in item_list:
# 	total += item['price'] * item['quantity']

# print the total price
print()
print("----------")
print(f"Total Price: {total} KWD")