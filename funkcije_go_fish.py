import random


def player_one_hand(deck):
    player_1_hand = []

    for i in range(7):
        card = random.choice(deck)
        deck.remove(card)
        player_1_hand.append(card)
    return player_1_hand


def player_one_points(cards):
    player_1_points = 0

    for card in cards:
        if cards.count(card) == 4:

            cards.remove(card)
            cards.remove(card)
            cards.remove(card)
            cards.remove(card)

            player_1_points += 1

    return player_1_points


def player_two_hand(deck):
    player_2_hand = []

    for i in range(7):
        card = random.choice(deck)
        deck.remove(card)
        player_2_hand.append(card)

    return player_2_hand


def player_two_points(cards):
    player_2_points = 0

    for card in cards:
        if cards.count(card) == 4:

            cards.remove(card)
            cards.remove(card)
            cards.remove(card)
            cards.remove(card)

            player_2_points += 1

    return player_2_points
