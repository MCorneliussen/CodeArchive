age = input("What is your current age? ")

x = 365 * (90 - int(age))
y = 52 * (90 - int(age))
z = 12 * (90 - int(age))
print(f"You have {x} days, {y} weeks, and {z} months left.")
