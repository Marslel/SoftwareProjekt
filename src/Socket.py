import time
import socketio
import json
import AIPlayer
import requests

sio = socketio.Client()
playerID = 0
hand = None
topCard = None
lastCard = None
lastMove = None
currentPlayer = None
handSize = None

@sio.event
def connect():
    """this event is triggerd, when the client connects to the server

    :return: a message
    """
    print('Connected')

@sio.event
def connectError(e):
    """this event is triggerd, when a connection error has accured

        :return: a message
        """
    print(e)


@sio.event
def disconnect():
    """this event is triggerd, when the client disconnect from the server

        :return: a message
        """
    print('Disconnected')

# In dieser Methode wird ein call ausgeführt der ein Tunier erstellt, mit der Anzahl der Best of Matches
def tournamentCreate(matches):
    """this Method post a tournamentcreation to the server with the number of matches

    :param matches: must be a positive odd number
    :return: a message
    """
    message = sio.call("tournament:create", matches)
    print(message)

# Hier kann man ein vorhandenes Turnier erstellen mit der TurnierID
def tournamentJoin(tournamentID):
    """this Method post a join on a tournament to the server with the matching tournamentID

        :param tournamentID: must be a positive odd number
        :return: a message
        """
    message = sio.call("tournament:join", tournamentID)
    print(message)

# Hier kann man ein Tunier verlassen
def tournamentLeave():
    """This method post a leave to the server

    :return: a message
    """
    message = sio.call("tournament:leave")
    print(message)

# Hier kann man ein Tunier starten
def tournamentStart():
    """This method post a starting message to the server

    :return: a message
    """
    message = sio.call("tournament:start")
    print(message)

@sio.on("tournament:info")
def tournamentInfo(message, _):
    """When the server post new Information about the tournament, then the client reveice it

    :param message: the status of new created tournaments
    :param _:
    :return: the message
    """
    print("Information for the tournament: ")
    print(message['message'])
    print(message['status'])

@sio.on("tournament:playerInfo")
def playerInTournament(message, _):
    """In this post from the server, the client receives a status of all players in current tournaments

    :param message: the message
    :param _:
    :return: a message
    """
    print("Player in Tournament: ")
    print(message['message'])

@sio.on("list:tournaments")
def tournamentsList(message, _):
    """When the server post a tournamentList, than will the client see it

    :param message: a message
    :param _:
    :return: a message
    """
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
    """This Mehtod is triggered when the server post a new gameState in a progressing Match

    :param state: the current State of the game
    :param _:
    :return: updatet statecards
    """
    global topCard, hand, lastMove, currentPlayer, lastCard, player_id, handSize
    topCard = state['topCard']
    lastCard = state['lastTopCard']
    hand = state['hand']
    lastMove = state['lastMove']
    currentPlayer = state['currentPlayer']
    handSize = state['handSize']

@sio.on("game:makeMove")
def makeMove(data):
    """This method post a move to the server, when the KI calculatet a move

    :param data:
    :return:
    """
    global topCard, hand
    print(data['message'])
    move = AIPlayer.play_nope(hand, topCard, currentPlayer, lastMove, lastCard, handSize)
    time.sleep(0.5)
    return move



@sio.on("match:info")
def match_info(message, _):
    """Current game Info from the serrver

    :param message: the message
    :param _:
    :return: a message
    """
    print("MATCH INFO: ")
    print(message['message'])

    opp = message['match']['opponents']





def login(accessToken):
    """connect to the server with the own accessToken

    :param accessToken: a Authentificator for the server
    :return:
    """

    player = (accessToken.json()['user'])
    global playerID
    playerID = (player['id'])

    print(accessToken.json())
    # Hier stellt man eine Verbindung mit dem Server auf
    sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={'token': accessToken.json()["accessToken"]})



