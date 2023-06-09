import time
import socketio
import json
import AIPlayer
import requests

sio = socketio.Client()
playerID = 0
hand = None
topCard = None
last_topCard = None
last_move = None
current_player = None
handSize = None

@sio.event
def connect():
    print('Connected')

@sio.event
def connectError(e):
    print(e)


@sio.event
def disconnect():
    print('Disconnected')

# In dieser Methode wird ein call ausgeführt der ein Tunier erstellt, mit der Anzahl der Best of Matches
def tournamentCreate(matches):
    message = sio.call("tournament:create", matches)
    print(message)

# Hier kann man ein vorhandenes Turnier erstellen mit der TurnierID
def tournamentJoin(tournamentID):
    message = sio.call("tournament:join", tournamentID)
    print(message)

# Hier kann man ein Tunier verlassen
def tournamentLeave():
    message = sio.call("tournament:leave")
    print(message)

# Hier kann man ein Tunier starten
def tournamentStart():
    message = sio.call("tournament:start")
    print(message)

@sio.on("tournament:info")
def tournamentInfo(message, _):
    print("Information for the tournament: ")
    print(message['message'])
    print(message['status'])

@sio.on("tournament:playerInfo")
def playerInTournament(message, _):
    print("Player in Tournament: ")
    print(message['message'])

@sio.on("list:tournaments")
def tournamentsList(message, _):
    list = []
    ID = []
    print("List of Tournaments: ")
    for tournament in message:

        ID.append(tournament['id'])
        ID.append(tournament['status'])

        for player in tournament["players"]:
            ID.append(player["username"])

        list.append(ID)
        ID = []

    for i in list:
        print(i)

@sio.on('game:state')
def gameState(state, _):
    global topCard, hand, last_move, current_player, last_topCard, player_id, handSize
    topCard = state['topCard']
    last_topCard = state['lastTopCard']
    hand = state['hand']
    last_move = state['lastMove']
    current_player = state['currentPlayer']
    handSize = state['handSize']

@sio.on("game:makeMove")
def makeMove(data):
    global topCard, hand
    print(data['message'])
    move = AIPlayer.play_nope(hand, topCard, current_player, last_move, last_topCard, handSize)
    time.sleep(0.5)
    return move



@sio.on("match:info")
def match_info(message, _):
    print("MATCH INFO: ")
    print(message['message'])

    opp = message['match']['opponents']





def login(accessToken):

    player = (accessToken.json()['user'])
    global playerID
    playerID = (player['id'])

    print(accessToken.json())
    # Hier stellt man eine Verbindung mit dem Server auf
    sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={'token': accessToken.json()["accessToken"]})



