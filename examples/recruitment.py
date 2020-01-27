print("Welcome to the special recruitment program, please answer the following questions: ")

skills = ["Python", "C++", "Javascript", "Running", "Eating"]

cv = {}

cv["name"] = input("What's your name? ")
cv["age"] = int(input("How old are you? "))
cv["experience"] = int(input("How many year's of experience do you have? "))
cv["skills"] = []

print()
print("skills: ")
print(f"1. {skills[0]}")
print(f"2. {skills[1]}")
print(f"3. {skills[2]}")
print(f"4. {skills[3]}")
print(f"5. {skills[4]}")
print()

user_skill = int(input("Choose a skill from above by entering its number: ")) #parse the skill into an integer, so the user_skill is a number.

cv["skills"].append(skills[user_skill - 1])

user_skill = int(input("Choose another skill from above by entering its number: ")) 
cv["skills"].append(skills[user_skill - 1])

if (25 <= cv["age"] <= 40) and cv["experience"] >= 3 and "Python" in cv["skills"]:
	print(f"You have been accpeted, {cv['name']}!")
else: 
	print("You have been rejected.")