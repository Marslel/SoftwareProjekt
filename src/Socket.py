
import socketio
import json
import AIPlayer
import requests

sio = socketio.Client()
playerID = 0

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
    sio.emit("tournament:join", json.dumps({"tournamentId": tournamentID}))

# Hier kann man ein Tunier verlassen
def tournamentLeave():
    sio.emit("tournament:leave")

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
def gameState(state):
    print("NEW STATE!")
    AIPlayer.play_nope(state)


def makeMove(move):
    message = sio.emit("game:makeMove", move)
    if message.status_code == 200:
        print("Erfolgreich an dem Server gesendet")
    else:
        return None



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



