print("Welcome to this rollercoaster!")
height = int(input("What is your height in centimeter?\n"))

bill = 0

if height >= 120: 
    print("You are tall enough for this rollercoaster. ")
    age = int(input("How old are you? \n"))
    if age < 12:
        bill += 5
        print(f"Child tickets are ${bill}. ")
    elif age <= 18:
        bill += 7
        print(f"Teen tickets are ${bill}. ")
    elif age >= 45 and age <= 55: #Two conditions in this elif statement. AND OR & NOT.
        print(f"Old people get to go for free." )
    else:
        bill += 12
        print(f"old as balls pay ${bill}. ")
    
    wants_photo = input("Would you like a photo taken for an additional $3. type Y for yes or N for no.")
    if wants_photo == "Y":
        bill += 3
        
        print(f"Your final bill will be ${bill}")
else:
    print("You are not tall enough, please step out of the line.")


# > Greater than
# >= Greater than or equal to.
# < Lesser than
# <= Lesser or equal to.
# == Equal to, but not less or greater.