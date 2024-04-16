print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

answer = input("Would you like to go right or left?\nPlease type Right or Left. ")

if answer == "Left":
    answer = input("You walk for a bit until you see a river with a small house and a dock. Do you swim or do you wait? \nPlease Type Swim or Wait. ")
    if answer == "Wait":
        answer = input("You found a comfortable seat but you need to go to the bathroom.\nYou look around and see a Red door, a Yellow door and a Blue door.\n Please type Red, Yellow or Blue to choose a door. ")
        if answer == "Yellow":
            answer = input("Congratulations, you peed your pants but you also found the hidden treasure.\nGame Over! ")
        elif answer == "Red":
            print("You walked straight into fire and lost.\nGame Over! ")
        elif answer == "Blue":
            print("You were eaten by beasts and lost.\nGame Over! ")
            
        else:
            print("You messed up and lost.\nGame Over! ")
    else:
        print("You were attacked by a school of trout, you drown.\nGame Over! ")
else:
    print("You fell into a hole and was forgotten. Better luck next time.\nGame Over!")