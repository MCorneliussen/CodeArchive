import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") 

list_count = len(names) 

random = random.randint(0, list_count)
person = names[random] 

print(f"{person} is going to buy the meal today!")
