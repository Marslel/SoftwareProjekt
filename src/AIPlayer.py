import json


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


def play_nope(hand, topCard, stateCurrentPlayer, lastMove, lastTopCard, stateHandSize):
    currentPlayer = stateCurrentPlayer
    hands = hand
    handSize = stateHandSize
    currentCard = topCard


    # Überprüfen, ob currentPlayerIdx unserer ID entspricht
    if currentPlayer['username'] == "Marsle" or currentPlayer['username'] == "Marsle2":
        print(f"\n{currentPlayer['username']}'s turn:")

        moveData = Move(None, None, None, None, 'reason_value')

        if currentCard:
            print(f"Current card: {currentCard}\n")

        for i in range(handSize):
            print(f"my card: {hands[i]}\n")



        if currentCard['type'] == 'number':
            moveData = numCards(currentCard, hands)

        if currentCard['type'] == 'see-through':
            moveData = seeTrough(lastTopCard, hands)

        if currentCard['type'] == 'reboot':
            moveData = Move('put', hand[0], None, None, 'reason_value')

        if currentCard['type'] == 'joker':
            moveData = Move('put', hand[0], None, None, 'reason_value')

        if moveData is None:
            if lastMove is not None:
                if lastMove['type'] == 'take':
                    moveData = Move('nope', None, None, None, 'reason_value')
                else:
                    moveData = Move('take', None, None, None, 'reason_value')


        # JSON-Datei schreiben
        with open('move.json', 'w') as file:
            json.dump(moveData.__dict__, file)

        with open('move.json', 'r') as file:
            jsonData = json.load(file)

        print("I play")
        print(jsonData)
        return jsonData

    else:
        print("It's not our turn.")
        return None


def numCards(topCard, hand):
    firstCard = None
    secondCard = None
    thirdCard = None
    value = 0
    cardValue = int(topCard['value'])

    searchCards = topCard['color'].split('-')
    fitCard = []

    for searchCard in searchCards:
        for cards in hand:
            if any(color in cards['color'].split('-') for color in searchCard.split('-')) and cards['type'] == 'number':
                fitCard.append(cards)
                value += 1
        if len(fitCard) >= cardValue:
            break
        else:
            countJoker = jokerAvailable(hand)
            countReboot = rebootAvailable(hand)
            countSeeTrough = seeTroughAvailable(hand)
            if countJoker > 0 and (countJoker + value) >= cardValue:
                moveData = playJoker(fitCard, countJoker, cardValue)
                return moveData
            elif countReboot > 0:
                moveData = playReboot()
                return moveData
            elif countSeeTrough > 0:
                cardsSeeTrough = canPlaySeeTrough(hand, fitCard, searchCards)
                if len(cardsSeeTrough) > 0:
                    moveData = playSeeTrough(cardsSeeTrough)
                    return moveData
            fitCard.clear()
            value = 0

    # Wenn man genug Karten hat, dann können die rausgelegt werden
    if value >= cardValue:
        if cardValue >= 3:
            thirdCard = fitCard[2]

            cardValue -= 1

        if cardValue >= 2:
            secondCard = fitCard[1]
            cardValue -= 1

        if cardValue >= 1:
            firstCard = fitCard[0]


        moveData = Move("put", firstCard, secondCard, thirdCard, 'reason_value')
        return moveData
        # Meine Karten Anzahl ist zu gering
    return None

def seeTrough(lastCard, hand):
    moveData = None
    if lastCard['type'] == 'reboot':
        moveData = reboot(hand)
    elif lastCard['type'] == 'number':
        moveData = numCards(lastCard, hand)
    elif lastCard['type'] == 'joker':
        moveData = Move('put', hand[0], None, None, 'reason_value')
    elif lastCard['type'] == 'see-through':
        moveData = seeTroughUnderSeeTrough(lastCard, hand)
    return moveData

def seeTroughUnderSeeTrough(lastCard, hand):
    for cards in hand:
        if lastCard['color'] in cards['color'].split("-"):
            moveData = Move('put', cards, None, None, 'reason_value')
            break
    return moveData


def reboot(hand):
    moveData = Move('put', hand[0], None, None, 'reason_value')
    return moveData

def jokerAvailable(hand):
    count = 0
    for cards in hand:
        if cards['type'] == 'joker':
            count+=1
    return count

def rebootAvailable(hand):
    count = 0
    for cards in hand:
        if cards['type'] == 'reboot':
            count += 1
    return count

def seeTroughAvailable(hand):
    count = 0
    for cards in hand:
        if cards['type'] == 'see-through':
            count += 1
    return count

def playJoker(fitCard, countJoker, cardValue):
    joker = {
        "type": "joker",
        "color": "multi",
        "value": 1,
        "select?": None,
        "selectValue?": None,
        "selectedColor?": None
    }
    if cardValue == 3:
        if countJoker == 3:
            moveData = Move('put', joker, joker, joker, 'reason_value')
        elif countJoker == 2:
            moveData = Move('put', fitCard[0], joker, joker, 'reason_value')
        else:
            moveData = Move('put', fitCard[0], fitCard[1], joker, 'reason_value')
    elif cardValue == 2:
        if countJoker == 2:
            moveData = Move('put', joker, joker, None, 'reason_value')
        else:
            moveData = Move('put', fitCard[0], joker, None, 'reason_value')
    else:
        moveData = Move('put', joker, None, None, 'reason_value')

    return moveData

def playReboot():
    reboot = {
        "type": "reboot",
        "color": "multi",
        "value": None,
        "select?": None,
        "selectValue?": None,
        "selectedColor?": None
    }
    moveData = Move('put', reboot, None, None, 'reason_value')
    return moveData

def canPlaySeeTrough(hand, fitCard, searchedCards):
    allSeeTroughCards = []
    for searchedCard in searchedCards:
        for card in hand:
            if card['type'] == 'see-through' and any(color in card['color'] for color in searchedCard.split('-')):
                allSeeTroughCards.append(card)
    return allSeeTroughCards

def playSeeTrough(allSeeTrough):
    moveData = Move('put', allSeeTrough[0], None, None, 'reason_value')

    return moveData
