bill = float(input("Please enter the total amount to pay $ :\n"))
split = int(input("How many people are paying? :\n"))
tip = int(input("How much would you like to tip? 10, 15, 20? :\n"))


tip_percentage = tip / 100
tip_amount = bill * tip_percentage
total_bill = bill + tip_amount
per_pers = total_bill / split

result = "{:.2f}".format(per_pers)

print(f"the total amount to pay per person is ${result}")