def greeting(name):
	print(f"Hello {name}!")

greeting("Dave")
# greeting("Steve")

def multiply(x, y):
	return x * y

# print(multiply(3,4))
result = multiply(3,4)

# print(result)
# scope concept example: x is defind outside the function, do it will be printed using print function. otherwise, an error will br displayed on the terminal
x = 5
def example():
	x = 20
	print(x)
example()
print(x)

wallet = 259.695

# print(wallet)
print(f"{wallet: .2f}") #prints two Decimals only