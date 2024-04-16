import random

def deal_card():
    '''This function returns a random card from the cards list.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_of_cards):
    '''This function calculates the total score of each player and it checks if the user has blackjack, it also converts ace to 1 if score is over 21 and returns result.'''
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)

def compare(user_score, computer_score):
    '''This function compares the user and computer score and returns the result/declares the winner'''
    if user_score == computer_score:
        return "It's a draw "
    elif computer_score == 0:
        return "You lost, your opponent has Blackjack "
    elif user_score == 0:
        return "You win, you have Blackjack! "
    elif user_score > 21:
        return "You lost, you went over 21. "
    elif computer_score > 21:
        return "You win, opponent went over 21! "
    elif user_score > computer_score:
        return "You win, with the highest card score. "
    else:
        return "You lost, with the lowest card score. "

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("'y' to get another card or 'n' to pass. ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"\nYour final hand: {user_cards} & score: {user_score}")
    print(f"The opponents hand: {computer_cards} & score: {computer_score}\n")
    print(compare(user_score, computer_score))

while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

