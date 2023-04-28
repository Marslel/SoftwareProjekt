import asyncio
import socketio
import sys

sio = socketio.Server()


@sio.event
def connect():
    print('Connected')
    result = sio.call('sum', {'numbers': [1, 2]})
    print(result)

@sio.event
def connectError(e):
    print(e)


@sio.event
def disconnect():
    print('Disconnected')

@sio.event
def mult(data):
    return data['numbers'][0] * data['numbers'][1]

@sio.event
def clientCount(count):
    print('There are', count, 'connected clients')


@sio.event
def roomCount(count):
    print('There are', count, 'clients in my room')

@sio.event
def userJoined(username):
    print('User', username, 'has joined.')

@sio.event
def userLeft(username):
    print('User', username, 'has left.')

def main(username):
    sio.connect('http://localhost:8000', headers={'X-Username': username})

    sio.wait()

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)



def client():
    sio = socketio.Client()


if __name__ == '__main__':
    client()
