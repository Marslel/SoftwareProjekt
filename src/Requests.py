import requests


def login(username, password):
    """the login Post to the server

    :param username: the given username for the login
    :param password: the given password for the login
    :return: accessToken for the server Authenticator
    """
    #Login Daten
    data = {'username': username, 'password': password}

    #Der Post request zum Login
    access = requests.post('https://nope-server.azurewebsites.net/api/auth/login', json=data)


    #Abfrage ob man sich einloggen konnte
    if access.status_code == 200:
        return access
    else:
        return None


def register(username, password, firstName, lastName):
    """The register Post to the server

    :param username: the given username for the login
    :param password: the given password for the login
    :param firstName: the given firstName for the login
    :param lastName: the given lastName for the login
    :return: the success message from the server
    """
    data = {'username': username, 'password': password, 'firstname': firstName, 'lastname': lastName}

    message = requests.post('https://nope-server.azurewebsites.net/api/auth/register', json=data)

    return message

