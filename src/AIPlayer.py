import random
import json

#Schnittstelle noch hinzufügen
def play_nope(state, userID):

    players = state['players']
    currentPlayerIDx = state['currentPlayerIdx']
    currentPlayer = players[currentPlayerIDx]
    hands = state['hand'][currentPlayerIDx]
    currentCard = state['topCard']
    nopeUsed = False

    # Überprüfen, ob currentPlayerIdx unserer ID entspricht
    if currentPlayer['id'] == userID:
        print(f"\n{currentPlayer['username']}'s turn:")
        print(f"Your hand: {hands}")

        if currentCard:
            print(f"Current card: {currentCard}")

        action = get_player_action()

        if action == 'play':
            card_index = get_card_to_play(hands)
            if card_index is None:
                print("Invalid card.")
                return

            currentCard = hands[card_index]
            del hands[card_index]
            nopeUsed = False

        elif action == 'nope':
            if not currentCard or nopeUsed:
                print("Cannot use Nope card.")
                return

            nopeUsed = True

        else:
            print("Invalid action.")
            return

        # HIER muss die post Schnittstelle hin


    else:
        print("It's not our turn.")


def get_player_action():
    randomInt = random.randint(0, 1)
    action = ['play', 'nope']
    return action[randomInt]


def get_card_to_play(hand):
    while True:
        card_index = random.randint(0, len(hand))
        if card_index in range(len(hand)):
            return card_index


play_nope()
