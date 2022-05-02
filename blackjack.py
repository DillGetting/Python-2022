import random
import os
import time


# The Card class definition
class Card:
    def __init__(self, suit, value, card_value):
        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing Value of the Card like A for Ace, K for King
        self.value = value

        # Score Value for the Card like 10 for King
        self.card_value = card_value


# Clear the terminal
def clear():
    os.system("clear")


# Function to print the cards
def print_cards(cards, hidden):
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()


# Function for a single game of blackjack
def blackjack_game(deck):
    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []

    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0

    clear()

    # Initial dealing for player and dealer
    while len(player_cards) < 2:

        # Randomly dealing a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)

        # Updating the player score
        player_score += player_card.card_value

        # In case both the cards are Ace, make the first ace value as 1
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

        # Print player cards and score
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        input()

        # Randomly dealing a card
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        # Updating the dealer score
        dealer_score += dealer_card.card_value

        # Print dealer cards and score, keeping in mind to hide the second card and score
        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALER SCORE = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

        # In case both the cards are Ace, make the second ace value as 1
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10

        input()

    # Player gets a blackjack
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        quit()

    clear()

    # Print dealer and player cards
    print("DEALER CARDS: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

    print()

    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    # Managing the player moves
    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")

        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Wrong choice!! Try Again")

        # If player decides to HIT
        if choice.upper() == 'H':

            # Dealing a new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            # Updating player score
            player_score += player_card.card_value

            # Updating player score in case player's card have ace in them
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1

            clear()

            # Print player and dealer cards
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)

            print()

            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)

        # If player decides to Stand
        if choice.upper() == 'S':
            break

    clear()

    # Print player and dealer cards
    print("PLAYER CARDS: ")
    print_cards(player_cards, False)
    print("PLAYER SCORE = ", player_score)

    print()
    print("DEALER IS REVEALING THE CARDS....")

    print("DEALER CARDS: ")
    print_cards(dealer_cards, False)
    print("DEALER SCORE = ", dealer_score)

    # Check if player has a Blackjack
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK")
        quit()

    # Check if player busts
    if player_score > 21:
        print("PLAYER BUSTED!!! GAME OVER!!!")
        quit()

    input()

    # Managing the dealer moves
    while dealer_score < 17:
        clear()

        print("DEALER DECIDES TO HIT.....")

        # Dealing card for dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)

        # Updating the dealer's score
        dealer_score += dealer_card.card_value

        # Updating player score in case player's card have ace in them
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1

        # print player and dealer cards
        print("PLAYER CARDS: ")
        print_cards(player_cards, False)
        print("PLAYER SCORE = ", player_score)

        print()

        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)

        input()

    # Dealer busts
    if dealer_score > 21:
        print("DEALER BUSTED!!! YOU WIN!!!")
        quit()

        # Dealer gets a blackjack
    if dealer_score == 21:
        print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")
        quit()

    # TIE Game
    if dealer_score == player_score:
        print("TIE GAME!!!!")

    # Player Wins
    elif player_score > dealer_score:
        print("PLAYER WINS!!!")

        # Dealer Wins
    else:
        print("DEALER WINS!!!")


if __name__ == '__main__':

    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

    # The suit value
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}

    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # The card value
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                    "K": 10}

    # The deck of cards
    deck = []

    # Loop for every type of suit
    for suit in suits:

        # Loop for every type of card in a suit
        for card in cards:
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    blackjack_game(deck)
