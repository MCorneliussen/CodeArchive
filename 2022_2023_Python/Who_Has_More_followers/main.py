from data import *
import random
from art import logo, vs
import os

def summon_data():
  return random.choice(data)

def format_data(compare_this_profile):
  name = compare_this_profile["name"]
  description = compare_this_profile["description"]
  country = compare_this_profile["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_is_running = True
  profile_a = summon_data()
  profile_b = summon_data()

  while game_is_running:
    profile_a = profile_b
    profile_b = summon_data()

    while profile_a == profile_b:
      profile_b = summon_data()

    print(f"Compare A: {format_data(profile_a)}.")
    print(vs)
    print(f"Against B: {format_data(profile_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = profile_a["follower_count"]
    b_follower_count = profile_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system('cls')
    print(logo)
    if is_correct:
      score += 1
      print(f"You are right! Current score: {score}.")
    else:
      game_is_running = False
      print(f"You guessed wrong and lose, Final score: {score}")

game()

