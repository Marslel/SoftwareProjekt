import requests

#data = {'username': 'Marsle', 'password': 'Software', 'firstname': 'Marcel', 'lastname': 'Bergen'}


def login():
    #Login Daten
    data = {'username': 'Marsle', 'password': 'Software'}

    #Der Post request zum Login
    r = requests.post('https://nope-server.azurewebsites.net/api/auth/login', json=data)

    #Der Accestoken zur Authentifizierung
    return r
