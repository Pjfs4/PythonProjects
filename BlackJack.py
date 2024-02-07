import random


def dealing():
    """Returns a random card from the deck!"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calculates the sum of the player cards or the sum of the computer cards"""
    soma = sum(cards)
    if soma == 21 and len(cards) == 2:
        return 0
    if 11 in cards and soma > 21:
        cards.remove(11)
        cards.append(1)
        soma = sum(cards)
        return soma
    else:
        return soma


def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Tie!"
    elif computer_score == 0:
        return "Your opponent has BlackJack, you lose!"
    elif user_score == 0:
        return "You have BlackJack, YOU WIN!!"
    elif user_score > 21:
        return "You went over 21, you lose!"
    elif computer_score > 21:
        return "Opponent went over 21, you WIN!!"
    elif user_score > computer_score:
        return "YOU WIN!!"
    else:
        return "You Lose!"


def play_blackjack():
    computers_cards = []
    my_cards = []
    is_game_over = False

    for _ in range(0, 2):
        my_cards.append(dealing())
        computers_cards.append(dealing())

    count = calculate_score(my_cards)
    computers_count = calculate_score(computers_cards)
    print(f"Your cards are: {my_cards}, current score: {count}")
    print(f"computer's first card: {computers_cards[0]}")

    while not is_game_over:
        if count == 0 or computers_count == 0 or count > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card or 'n' to pass: ")
            if another_card.lower() == 'y':
                my_cards.append(dealing())
                count = calculate_score(my_cards)
                print(f"Your cards are: {my_cards}, current score: {count}")

            else:
                is_game_over = True
    if count <= 21:
        while computers_count != 0 and computers_count < 17:
            computers_cards.append(dealing())
            computers_count = calculate_score(computers_cards)

    print(f"\nComputers cards are: {computers_cards}, with a count of: {computers_count}")
    print(f"Your final hand is: {my_cards}, with a count of: {count}\n")
    print(compare_scores(count, computers_count))

    while input("Do you want to restart the game? Type 'r' to Restart, press any key to exit: ") == "r":
        play_blackjack()


play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if play.lower() == 'y':
    play_blackjack()
