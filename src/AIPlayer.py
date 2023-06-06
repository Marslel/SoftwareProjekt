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

isTake = False
takeCard = 0
takeValue = 0
takeCardValue = 0

def play_nope(state):
    global isTake
    global takeCard
    global takeValue
    global takeCardValue
    players = state['players']
    currentPlayerIDx = state['currentPlayerIdx']
    currentPlayer = players[currentPlayerIDx]
    hands = HAND['hand']
    handSize = state['handSize']
    currentCard = state['topCard']
    nopeUsed = False

    type = []
    firstCard = [0]
    secondCard = [0]
    thirdCard = [0]

    # Überprüfen, ob currentPlayerIdx unserer ID entspricht
    if currentPlayer['username'] == "Marsle":
        if not isTake:
            print(f"\n{currentPlayer['username']}'s turn:")

            if currentCard:
                print(f"Current card: {currentCard}")

            value = 0
            index = []
            cardValue = int(currentCard['value'])
            for i in range(handSize):
                if hands[i]['color'] == currentCard['color']:
                    color = hands[i]['color']
                    print(f"\n{color}")
                    index.append(i)
                    value += 1

            #Wenn man genug Karten hat, dann können die rausgelegt werden
            if value >= cardValue:
                if value >= 3:
                    thirdCard.remove(0)
                    thirdCard = hands[index[2]]

                    value -= 1

                if value >= 2:
                    secondCard.remove(0)
                    secondCard.append(hands[index[1]])
                    value -= 1

                if value >= 1:
                    firstCard.remove(0)
                    firstCard.append(hands[index[0]])

                type.append("put")
                moveData = Move(type[0], firstCard[0], secondCard[0], thirdCard, 'reason_value')
            #Meine Karten Anzahl ist zu gering
            else:
                type.append("take")
                isTake = True
                takeCard = currentCard['color']
                takeValue = value
                takeCardValue = cardValue
                moveData = Move(type[0], firstCard[0], secondCard[0], thirdCard[0], 'reason_value')
        # Nope Fall
        else:
            index = []
            #Hier wird geschaut ob die neu gezogene Karte die richtige Farbe hat
            if hands[handSize-1]['color'] == takeCard:
                takeValue +=1
                for i in range(handSize):
                    if hands[i]['color'] == takeCard:
                        index.append(i)
                # Wenn man genug Karten hat, dann können die rausgelegt werden
                if takeValue == takeCardValue:
                    if takeValue >= 3:
                        thirdCard.remove(0)
                        thirdCard = hands[index[2]]

                        takeValue -= 1

                    if takeValue >= 2:
                        secondCard.remove(0)
                        secondCard.append(hands[index[1]])
                        takeValue -= 1

                    if takeValue >= 1:
                        firstCard.remove(0)
                        firstCard.append(hands[index[0]])

                    type.append("put")
                    moveData = Move(type[0], firstCard[0], secondCard[0], thirdCard, 'reason_value')
                #Sonst wird Nope gespielt
                else:
                    print("Hier Nope")
                    moveData = Move("nope", 0, 0, 0, 'Use nope')
            #Sonst wird Nope gespielt
            else:
                print("Oder Hier Nope")
                moveData = Move("nope", 0, 0, 0, 'Use nope')


        # JSON-Datei schreiben
        with open('move.json', 'w') as file:
            json.dump(moveData.__dict__, file)

        with open('move.json', 'r') as file:
            jsonData = json.load(file)

        # Socket.makeMove(jsonData)

    else:
        print("It's not our turn.")