from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

auctioneers = {}
def new_bid(name, amount):
  auctioneers[name] = amount 

program_run = True

while program_run is True:
  name = input("Please enter your name.\n")
  amount = input("How much would you like to bid?\n$")
  new_bid(name, amount)
  program_run = input("Are there any more bidders? please type yes or no\n").lower()
  if program_run == "no":
      program_run = False
  else:
      clear()
      program_run = True

max_value = max(auctioneers.values())
max_key = max(auctioneers, key=auctioneers.get)

print(f"The winner is {max_key} with a bid of ${max_value}")
