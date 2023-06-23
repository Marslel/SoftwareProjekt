"""
In dieser Klasse wird die GUI erstellt, um das Kartenspiel Nope zu spielen

@author Marcel Bergen
"""
import tkinter
import tkinter as tk
from tkinter import messagebox
from Requests import *
import Socket

access = 0
data = 0

class MainWindow(tk.Tk):
    """
    This class controlls the Frames that are active, aswell as all the logic for the different Buttons
    """
    def __init__(self, *args, **kwargs):
        """this Method controlls the frames and adds new classes

        :param args:
        :param kwargs:
        """
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Hier werden alle Frames in einem Container gepackt
        for F in (Login, Register, GameMenu, PlayGame, History, Tournament):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Diese Methode ruft bei dem Programmstart den Login Screen zuerst auf
        self.showFrame(Login)

    # Diese Methode schaut nach ob ein bereits registrierter User sich anmeldet
    def login(self, usernameEntry, passwordEntry):
        """this Method creates a login post to the server

        :param usernameEntry: This is the username that the user enters
        :param passwordEntry: This is the password that the user enters
        :return:
        """
        username = "Marsle"
        username2 = "Marsle2"
        password = "Software"
        if usernameEntry.get() == username or usernameEntry.get() == username2 and passwordEntry.get() == password:
            # Aus der Klasse Request wird die Login methode verwendet um den Access key zu erhalten
            if usernameEntry.get() == "Marsle":
                access = login(username, password)
            else:
                access = login(username2, password)
            print("Successfully logged in")
            Socket.login(access)
            self.showFrame(GameMenu)
        else:
            messagebox.showerror(title="Error", message="Failed to login.")

    # In dieser Methode kann sich ein neuer Benutzer sich registrieren
    def register(self, username, password, firstName, lastName):
        """This method post a register request to the server

        :param username: is the name that the user enters
        :param password: is the password that the user enters
        :param firstName: is the firstname that the user enters
        :param lastName: is the lastname that the user enters
        :return:
        """
        register(username, password, firstName, lastName)
        messagebox.showinfo(title="Success", message="New player created")
        self.showFrame(Login)

    # In dieser Methode kann man ein Tournier betretentitlescreen
    def joinTournament(self):
        """This method post a join request to a tournament to the server

        :return:
        """
        tournamentID = input("Tournament-ID: ")
        Socket.tournamentJoin(tournamentID)
        print("Tournament joined")

    # In dieser Methode kann man ein Tunrier erstellen
    def createTournament(self):
        """This Method post a creation of a tournament to the server

        :return:
        """
        matches = int(input("Insert the number of matches: "))
        Socket.tournamentCreate(matches)
        print("Create Tournament")

    # In dieser Methode kann man ein Turnier verlassen
    def leaveTournament(self):
        """This Method post a leave request to the Server

        :return:
        """
        Socket.tournamentLeave()
        print("leaving")

    def startTournament(self):
        """This Method post a start request to the Server

        :return:
        """
        Socket.tournamentStart()
        print("Start Game")

    # Diese Methode zeigt den aktuellen Frame
    def showFrame(self, cont):
        """ This Method shows the current frame

        :param cont:
        :return:
        """
        frame = self.frames[cont]
        frame.tkraise()


# Diese Klasse ist der Haupt Screen und man kann sich hier einloggen
class Login(tk.Frame):
    """This class construct the Login frame

    """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Widgets erstellen
        loginLabel = tkinter.Label(self, text="Login", bg='#878787', fg='#FFFFFF', font=("Arial", 30))
        usernameLabel = tkinter.Label(self, text="Username", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        usernameEntry = tkinter.Entry(self, font=("Arial", 30))
        passwordLabel = tkinter.Label(self, text="Password", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        passwordEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        loginButton = tkinter.Button(self, text="Login", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                     command=lambda: controller.login(usernameEntry, passwordEntry))
        registerButton = tkinter.Button(self, text="Register", bg='#666666', fg='#FFFFFF', font=("Arial", 17),
                                        command=lambda: controller.showFrame(Register))

        # Widgets in der richtigen Position bringen
        loginLabel.grid(row=0, column=0, columnspan=60, sticky="news", pady=40)
        usernameLabel.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1, pady=20)
        passwordLabel.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1, pady=20)
        loginButton.grid(row=3, column=0, columnspan=5, pady=30)
        registerButton.grid(row=4, column=2, columnspan=1, pady=5)


# Mit dieser Klasse können sich neue Benutzer sich registrieren
class Register(tk.Frame):
    """This class construct the Register frame

        """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Widgets erstellen
        registerLabel = tkinter.Label(self, text="Register", bg='#878787', fg='#FFFFFF', font=("Arial", 30))
        usernameLabel = tkinter.Label(self, text="Username", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        usernameEntry = tkinter.Entry(self, font=("Arial", 30))
        passwordLabel = tkinter.Label(self, text="Password", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        passwordEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        firstNameLabel = tkinter.Label(self, text="Firstname", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        firstNameEntry = tkinter.Entry(self, font=("Arial", 30))
        lastNameLabel = tkinter.Label(self, text="Lastname", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        lastNameEntry = tkinter.Entry(self, font=("Arial", 30))
        RegisterButton = tkinter.Button(self, text="Register", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                        command=lambda: controller.register(usernameEntry, passwordEntry,
                                                                            firstNameEntry, lastNameEntry))

        # Widgets in der richtigen Position bringen
        registerLabel.grid(row=0, column=1, columnspan=5, sticky="news", padx=190, pady=20)
        usernameLabel.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1, pady=10)
        passwordLabel.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1, pady=10)
        firstNameLabel.grid(row=3, column=0)
        firstNameEntry.grid(row=3, column=1, pady=10)
        lastNameLabel.grid(row=4, column=0)
        lastNameEntry.grid(row=4, column=1, pady=10)
        RegisterButton.grid(row=5, column=1, padx=180, pady=30)


# Diese Klasse spiegelt den Hauptscreen des Spieles wieder
class GameMenu(tk.Frame):
    """This class construct the GameMenu frame

        """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        gameLabel = tkinter.Label(self, text="Welcome to the Game", bg='#878787', fg='#FFFFFF', font=("Arial", 30))

        gameStartButton = tkinter.Button(self, text="Play", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                         command=lambda: controller.startTournament())

        gameHistoryButton = tkinter.Button(self, text="History", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                         command=lambda: controller.showFrame(History))

        titlescreenButton = tkinter.Button(self, text="Titlescreen", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                           command=lambda: controller.showFrame(Login))

        tournamentButton = tkinter.Button(self, text="Tournament", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                           command=lambda: controller.showFrame(Tournament))

        gameLabel.grid(row=0, column=2, columnspan=5, sticky="news", pady=20)
        gameStartButton.grid(row=3, column=6, padx=0, pady=0)
        gameHistoryButton.grid(row=4, column=6, padx=0, pady=30)
        tournamentButton.grid(row=5, column=6, padx=0, pady=0)
        titlescreenButton.grid(row=6, column=6, padx=250, pady=30)

# In dieser KLasse wird man das eigentliche Spiel spielen
class PlayGame(tk.Frame):
    """This class construct the PlayGame frame

        """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuButton = tkinter.Button(self, text="Back to Menu", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                    command=lambda: controller.showFrame(GameMenu))

        menuButton.grid(row=500, column=6, padx=200, pady=390)

# In dieser Klasse kann man alle gespielten Spiele sehen
class History(tk.Frame):
    """This class construct the History frame

        """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuButton = tkinter.Button(self, text="Back to Menu", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                    command=lambda: controller.showFrame(GameMenu))

        menuButton.grid(row=500, column=6, padx=200, pady=390)

# in Dieser Klasse kann man ein Turnier erstellen und eintreten
class Tournament(tk.Frame):
    """This class construct the Tournament frame

        """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tournamentLabel = tkinter.Label(self, text="Tournament Menu", bg='#878787', fg='#FFFFFF', font=("Arial", 30))

        joinTournamentButton = tkinter.Button(self, text="Join", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                    command=lambda: controller.joinTournament())

        createTournamentButton = tkinter.Button(self, text="Create", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                              command=lambda: controller.createTournament())

        leaveTournamentButton = tkinter.Button(self, text="Leave", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                              command=lambda: controller.leaveTournament())

        menuButton = tkinter.Button(self, text="Back to Menu", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                    command=lambda: controller.showFrame(GameMenu))

        tournamentLabel.grid(row=0, column=6, padx=200, pady=20)
        joinTournamentButton.grid(row=1, column=6, padx=200, pady=10)
        createTournamentButton.grid(row=2, column=6, padx=200, pady=10)
        leaveTournamentButton.grid(row=3, column=6, padx=200, pady=10)
        menuButton.grid(row=500, column=6, padx=200, pady=10)

class PlayTournament(tk.Frame):
    """This class construct the playTournament frame

        """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


if __name__ == "__main__":
    """This is the start of the programm
    """
    window = MainWindow()
    window.title("Cardgame-Nope")
    window.geometry("680x520")
    window.mainloop()
