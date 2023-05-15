
import socketio
import json

sio = socketio.Client()

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
def leave_tournament():
    sio.emit("tournament:leave")

# Hier kann man ein Tunier starten
def start_tournament():
    message = sio.call("tournament:start")
    print(message)

def gameState():
    state = sio.emit("game:state")
    return state

def makeMove(move):
    message = sio.call("game:makeMove", move)
    print(message)

def main(accessToken):
    # Hier stellt man eine Verbindung mit dem Server auf
    sio.connect("https://nope-server.azurewebsites.net", auth={'token': accessToken})

    sio.wait()


