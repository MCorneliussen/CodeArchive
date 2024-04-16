#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇
flip = random.randint(0, 1)

if flip == 0:
    print("Heads")
elif flip == 1:
    print("Tails")
