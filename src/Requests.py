import requests

#data = {'username': 'Marsle', 'password': 'Software', 'firstname': 'Marcel', 'lastname': 'Bergen'}


def login(username, password):
    #Login Daten
    data = {'username': username, 'password': password}

    #Der Post request zum Login
    access = requests.post('https://nope-server.azurewebsites.net/api/auth/login', json=data)

    #Der Accestoken zur Authentifizierung
    return access

def register(username, password, firstName, lastName):

    data = {'username': username, 'password': password, 'firstname': firstName, 'lastname': lastName}

    message = requests.post('https://nope-server.azurewebsites.net/api/auth/register', json=data)

    return message