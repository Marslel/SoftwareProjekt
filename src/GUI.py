import tkinter
import tkinter as tk
from tkinter import messagebox
import Requests


class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        print("test")
        for F in (Login, Register, Game):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        print("test1")
        self.showFrame(Login)
        print("test2")

    def login(self, usernameEntry, passwordEntry):
        username = "Marsle"
        password = "Software"
        if usernameEntry.get() == username and passwordEntry.get() == password:
            access = Requests.login(username, password)
            print("Successfully logged in")
            print(access.text)
            self.showFrame(Game)
        else:
            messagebox.showerror(title="Error", message="Failed to login.")

    def register(self, username, password, firstName, lastName):
        Requests.register(username, password, firstName, lastName)
        messagebox.showinfo(title="Success", message="New player created")
        self.showFrame(Login)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        print("hallo")

        # Widgets erstellen
        loginLabel = tkinter.Label(self, text="Login", bg='#878787', fg='#FFFFFF', font=("Arial", 30))
        usernameLabel = tkinter.Label(self, text="Username", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        usernameEntry = tkinter.Entry(self, font=("Arial", 30))
        passwordLabel = tkinter.Label(self, text="Password", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        passwordEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        loginButton = tkinter.Button(self, text="Login", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                     command=lambda: controller.login(usernameEntry, passwordEntry))
        registerButton = tkinter.Button(self, text="Register", bg='#666666', fg='#FFFFFF', font=("Arial", 20),
                                        command=lambda: controller.showFrame(Register))

        loginLabel.pack()
        usernameLabel.pack()
        usernameEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()
        loginButton.pack()
        registerButton.pack()

        # Widgets in der richtigen Position bringen
        '''
        loginLabel.grid(row=0, column=0, columnspan=5, sticky="news", pady=40)
        usernameLabel.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1, pady=20)
        passwordLabel.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1, pady=20)
        loginButton.grid(row=3, column=0, columnspan=5, pady=30)
        registerButton.grid(row=4, column=3, columnspan=5, pady=5)
        '''


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        print("hallo1")
        # Widgets erstellen
        registerLabel = tkinter.Label(self, text="Login", bg='#878787', fg='#FFFFFF', font=("Arial", 30))
        usernameLabel = tkinter.Label(self, text="Username", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        usernameEntry = tkinter.Entry(self, font=("Arial", 30))
        passwordLabel = tkinter.Label(self, text="Password", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        passwordEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        firstNameLabel = tkinter.Label(self, text="Firstname", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        firstNameEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        lastNameLabel = tkinter.Label(self, text="Lastname", bg='#878787', fg='#FFFFFF', font=("Arial", 16))
        lastNameEntry = tkinter.Entry(self, show="*", font=("Arial", 30))
        RegisterButton = tkinter.Button(self, text="Login", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                        command=lambda: controller.register(usernameEntry, passwordEntry,
                                                                            firstNameEntry, lastNameEntry))
        '''
        # Widgets in der richtigen Position bringen
        registerLabel.grid(row=0, column=0, columnspan=5, sticky="news", pady=40)
        usernameLabel.grid(row=1, column=0)
        usernameEntry.grid(row=1, column=1, pady=20)
        passwordLabel.grid(row=2, column=0)
        passwordEntry.grid(row=2, column=1, pady=20)
        firstNameLabel.grid(row=3, column=0)
        firstNameEntry.grid(row=3, column=1, pady=20)
        lastNameLabel.grid(row=4, column=0)
        lastNameEntry.grid(row=4, column=1, pady=20)
        RegisterButton.grid(row=5, column=0, columnspan=5, pady=30)
        '''
        registerLabel.pack()
        usernameLabel.pack()
        usernameEntry.pack()
        passwordLabel.pack()
        passwordEntry.pack()
        firstNameLabel.pack()
        firstNameEntry.pack()
        lastNameLabel.pack()
        lastNameEntry.pack()
        RegisterButton.pack()


class Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        print("hallo2")
        gameLabel = tkinter.Label(self, text="Wellcome to the Game", bg='#878787', fg='#FFFFFF', font=("Arial", 30))

        titlescreenButton = tkinter.Button(self, text="Titelscreen", bg='#666666', fg='#FFFFFF', font=("Arial", 30),
                                           command=lambda: controller.showFrame(Login))

        '''
        gameLabel.grid(row=0, column=0, columnspan=5, sticky="news", pady=40)
        titlescreenButton.grid(row=5, column=0, columnspan=5, pady=30)
        '''

        gameLabel.pack()
        titlescreenButton.pack()


window = MainWindow()
window.mainloop()
