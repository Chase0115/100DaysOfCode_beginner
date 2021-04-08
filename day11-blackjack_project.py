############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

from art import logo
import random
from replit import clear


def black_jack(a):
    if a == 21:
        return True
    else:
        return False


def final(u, c):
    print(f"Your final hand: {u}, final score: {sum(u)}")
    print(f"Computer's final hand: {c}, final score: {sum(c)}")


def ace(subject):
    for i in range(0, len(subject)):
        if sum(subject) > 21 and subject[i] == 11:
            subject[i] = 1
    return subject


def compare(u, c):
    if u > c:
        final(u, c)
        print("You win")
    elif u < c:
        final(u, c)
        print("Computer win")
    elif u == c:
        final(u, c)
        print("Draw")


def status(u, c):
    print(f"Your cards: {u}, current score: {sum(u)}")
    print(f"Computer's first card: {c[0]}")


print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play_game = input("Do you want to play Blackjack game? 'y' or 'n' : ").lower()

while play_game == 'y':
    clear()
    print(logo)

    user_deck = []
    com_deck = []
    user_deck.append(random.choice(cards))
    user_deck.append(random.choice(cards))
    com_deck.append(random.choice(cards))
    com_deck.append(random.choice(cards))

    status(user_deck, com_deck)

    if black_jack(sum(com_deck)):
        final(user_deck, com_deck)
        print("Computer is Blackjack. You lose.")
    elif black_jack(sum(user_deck)):
        final(user_deck, com_deck)
        print("You are Blackjack. You Win.")

    another_card = input(
        "Type 'y' to get another card, or 'n' to pass : ").lower()
    while another_card == 'y':
        user_deck.append(random.choice(cards))
        ace(user_deck)
        if sum(user_deck) > 21:
            final(user_deck, com_deck)
            print("Computer win.")
            break
        elif black_jack(sum(user_deck)):
            final(user_deck, com_deck)
            print("You are Blackjack. You Win.")
            break
        elif sum(user_deck) < 21:
            status(user_deck, com_deck)
            another_card = input(
                "Type 'y' to get another card, or 'n' to pass : ").lower()
    if another_card == 'n':
        while sum(com_deck) < 16:
            com_deck.append(random.choice(cards))
            ace(com_deck)
            if sum(com_deck) > 21:
                final(user_deck, com_deck)
                print("You win")
                break
            elif sum(com_deck) > sum(user_deck):
                final(user_deck, com_deck)
                print("Computer win")
                break
            else:
                final(user_deck, com_deck)
                print("You win")
                break
        if sum(com_deck) >= 16:
            compare(user_deck, com_deck)

    play_game = input("Do you want to play another game?'y' or 'n' : ").lower()
