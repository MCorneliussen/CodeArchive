import random

def game():
    def number():
        '''Function to give you a random integer between 1 and 100.'''
        random_number = random.randint(1, 100)
        return random_number

    def compare(user_guess, random_number):
        '''Function that checks if you guess correctly, too low or too high.'''
        if user_guess == random_number:
            return f"You guessed {user_guess} and that is correct, you win the game!"
        elif user_guess > random_number:
            return "Your guess is too high!"
        elif user_guess < random_number:
            return "Your guess is too low!"

    lives = 10
    random_number = number()
    still_playing = True

    difficulty = input("Please choose difficulty, 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        lives -= 5
    
    print("I'm thinking of a number between 1 and 100.")

    while still_playing:
        if lives == 0:
            print(f"You have {lives} attempts left, you lose.")
            still_playing = False
        elif lives > 0:       
            user_guess = int(input(f"{lives} attempts remaining, Please guess the number: "))
            lives -=1
            print(compare(user_guess, random_number))
            if user_guess == random_number:
                still_playing = False
                
while input("\nWould you like to play the number guessing game? 'y' or 'n': ") == "y":
    game()