from funkcije_go_fish import player_one_hand, player_one_points, player_two_hand, player_two_points
import random

deck = [
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace',
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace',
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace',
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace',
]

random.shuffle(deck)

player_one_cards = player_one_hand(deck)
player_two_cards = player_two_hand(deck)


player_one_score = player_one_points(player_one_cards)
player_two_score = player_two_points(player_two_cards)

player_one_total = 0
player_two_total = 0

player_one_total += player_one_score
player_two_total += player_two_score

while True:

    if len(player_two_cards) < 1:
        print("\nPlayer Two ran out of cards!")
        print("---GAME OVER---")
        break

    elif len(player_one_cards) < 1:
        print("\nPlayer One ran out of cards!")
        print("---GAME OVER---")
        break

    elif len(deck) < 1:
        print("\nDeck ran out of cards! GAME OVER!")

    while True:
        print("\n---PLAYER ONE PLAYING---")

        player_one_score = player_one_points(player_one_cards)

        player_one_cards.sort()

        print(player_one_cards)

        chosen_card = input("PLAYER ONE what is your chosen card? ")

        if chosen_card in player_two_cards:
            print(f"\nPLAYER TWO: I do have {chosen_card.upper()}!")

            for card in player_two_cards:
                if player_two_cards.count(chosen_card) >= 1:

                    player_two_cards.remove(chosen_card)
                    player_one_cards.append(chosen_card)

            player_one_score = player_one_points(player_one_cards)

            player_one_total += player_one_score

            msg = input("\nSee players stats? ")

            if msg == 'yes':

                player_one_cards.sort()
                player_two_cards.sort()

                print(
                    f"\nPLAYER ONE CARDS: {player_one_cards}, NUMBER OF CARDS: {len(player_one_cards)}")
                print(
                    f"PLAYER TWO CARDS: {player_two_cards}, NUMBER OF CARDS: {len(player_two_cards)}")

                print(f"\nPLAYER ONE TOTAL POINTS: {player_one_total}")
                print(f"PLAYER TWO TOTAL POINTS: {player_two_total}")

            if len(player_two_cards) < 1:
                break

            elif len(player_one_cards) < 1:
                break

            else:
                print("\nPLAYER ONE GOING AGAIN!")
                continue

        elif chosen_card not in player_two_cards:
            print(
                f"\nPLAYER TWO: I don't have {chosen_card.upper()}, GO FISH!")

            fished_card = deck[0]
            deck.remove(fished_card)
            player_one_cards.append(fished_card)

            player_one_score = player_one_points(player_one_cards)

            player_one_total += player_one_score

            msg = input("\nSee players stats? ")

            if msg == 'yes':

                player_one_cards.sort()
                player_two_cards.sort()

                print(
                    f"\nPLAYER ONE CARDS: {player_one_cards}, NUMBER OF CARDS: {len(player_one_cards)}")
                print(
                    f"PLAYER TWO CARDS: {player_two_cards}, NUMBER OF CARDS: {len(player_two_cards)}")
                print(f"PLAYER ONE TOTAL POINTS: {player_one_total}")
                print(f"PLAYER TWO TOTAL POINTS: {player_two_total}")
                print(f"CARDS IN THE DECK: {len(deck)}")

            if len(player_one_cards) < 1:
                break

            elif len(deck) < 1:
                break

            elif fished_card == chosen_card:
                print(
                    f"\nMy fished {fished_card.upper()} card matches my chosen {chosen_card.upper()} card, I can go again!!")
                continue

            elif fished_card != chosen_card:
                print(
                    f"\nMy fished {fished_card.upper()} card does not match my drawn {chosen_card.upper()} card, I can't continue!")
                break

    while True:

        if len(player_one_cards) < 1:
            break

        elif len(player_two_cards) < 1:
            break

        elif len(deck) < 1:
            break

        print("\n---PLAYER TWO PLAYING---")

        chosen_card = random.choice(player_two_cards)

        print(f"\nDo you have a {chosen_card.upper()}, PLAYER ONE?")

        msg = input(
            f"\nPLAYER ONE do you have {chosen_card.upper()}(yes/no)? ")

        if msg == 'yes':

            for card in player_one_cards:
                if player_one_cards.count(chosen_card) >= 1:

                    player_one_cards.remove(chosen_card)
                    player_two_cards.append(chosen_card)

            player_two_score = player_two_points(player_two_cards)

            player_two_total += player_two_score

            msg = input("\nSee player stats? ")

            if msg == 'yes':

                player_two_cards.sort()
                player_one_cards.sort()

                print(
                    f"\nPLAYER TWO CARDS: {player_two_cards}, NUMBER OF CARDS: {len(player_two_cards)}")
                print(
                    f"PLAYER ONE CARDS: {player_one_cards}, NUMBER OF CARDS: {len(player_one_cards)}")

                print(f"\nPLYER ONE TOTAL POINTS: {player_one_total}")
                print(f"PLAYER TWO TOTAL POINTS: {player_two_total}")

            if len(player_one_cards) < 1:
                break

            elif len(player_two_cards) < 1:
                break

            else:
                print("\nPLAYER TWO GOING AGAIN!")
                continue

        if msg == 'no':

            print(
                f"\nPLAYER ONE: I don't have {chosen_card.upper()}, GO FISH, PLAYER TWO!")

            fished_card = deck[0]
            deck.remove(fished_card)
            player_two_cards.append(fished_card)

            player_two_score = player_two_points(player_two_cards)

            player_two_total += player_two_score

            msg = input("\nSee player stats? ")

            if msg == 'yes':

                player_two_cards.sort()
                player_one_cards.sort()

                print(
                    f"\nPLAYER TWO CARDS: {player_two_cards}, NUMBER OF CARDS: {len(player_two_cards)}")
                print(
                    f"PLAYER ONE CARDS: {player_one_cards}, NUMBER OF CARDS: {len(player_one_cards)}")
                print(f"PLAYER TWO TOTAL POINTS: {player_two_total}")
                print(f"PLAYER ONE TOTAL POINTS: {player_one_total}")
                print(f"LENGTH OF DECK: {len(deck)}")

            if len(player_two_cards) < 1:
                break

            elif len(deck) < 1:
                break

            elif fished_card == chosen_card:
                print(
                    f"\nPLAYER TWO: My fished {fished_card.upper()} card matches my chosen {chosen_card.upper()} card, I can go again!!")
                continue

            elif fished_card != chosen_card:
                print(
                    f"\nPLAYER TWO: My fished {fished_card.upper()} card does not match my chosen {chosen_card.upper()} card, I can't continue!")
                break

if player_one_total > player_two_total:
    print(f"\nPLAYER ONE POINTS: {player_one_total}")
    print(f"PLAYER TWO POINTS: {player_two_total}")
    print("\n---PLAYER ONE HAS WON THE GAME!---")

elif player_two_total > player_one_total:
    print(f"\nPLAYER ONE POINTS: {player_one_total}")
    print(f"PLAYER TWO POINTS: {player_two_total}")
    print("\n---PLAYER TWO HAS WON THE GAME!---")

elif player_one_total == player_two_total:
    print(f"\nPLAYER ONE TOTAL POINTS: {player_one_total}")
    print(f"PLAYER TWO TOTAL POINTS: {player_two_total}")
    print("\n---GAME IS A TIE, BOTH PLAYERS HAVE SAME AMOUNT OF POINTS!!---")
