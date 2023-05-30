import random
import json
import Socket


# JSON-Datei lesen
with open('move.json', 'r') as file:
    json_data = json.load(file)

# JSON-Datei lesen
with open('stateTest.json', 'r') as file:
    state = json.load(file)

# JSON-Datei lesen
with open('hand.json', 'r') as file:
    HAND = json.load(file)

# Move-Objekt erstellen
class Move:
    def __init__(self, type, card1, card2, card3, reason):
        self.type = type
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.reason = reason



def play_nope(state):

    players = state['players']
    currentPlayerIDx = state['currentPlayerIdx']
    currentPlayer = players[currentPlayerIDx]
    hands = state['hand']
    handSize = state['handSize']
    currentCard = state['topCard']
    nopeUsed = False

    moveCard = 0
    # Überprüfen, ob currentPlayerIdx unserer ID entspricht
    if currentPlayer['username'] == "Marsle":
        print(f"\n{currentPlayer['username']}'s turn:")

        size = int(handSize)
        if currentCard:
            print(f"Current card: {currentCard}")

        isColor = False

        for i in range(handSize):
            if hands[i]['color'] == currentCard['color']:
                print("hello")
                color = hands[i]['color']
                print(f"\n{color}'")
                isColor = True
                break



        if isColor:
            count = int(currentCard['value'])

            for i in range(0, 1):
                print(i)
                if color == hands[i]['color'] and count != 0:
                    moveCard = hands[i]
                    count -= 1

            nopeUsed = False

        else:
            if not currentCard or nopeUsed:
                print("Cannot use Nope card.")
                return
            nopeUsed = True


        moveData = Move('put', moveCard, 'card2_value', 'card3_value', 'reason_value')

        # JSON-Datei schreiben
        with open('move.json', 'w') as file:
            json.dump(moveData.__dict__, file)

        with open('move.json', 'r') as file:
            jsonData = json.load(file)

        #Socket.makeMove(jsonData)

    else:
        print("It's not our turn.")



def get_card_to_play(hand, handSize):
    while True:
        card_index = random.randint(0, handSize)
        if card_index in range(len(hand)):
            return card_index

