import tkinter
import tkinter as tk
from tkinter import messagebox

# Erstellen Sie ein Fensterobjekt
window = tk.Tk()
window.title("Cardgame-Nope")
window.geometry("600x450")
window.configure(bg='#878787')


def login():
    username = "Marsle"
    password = "Software"
    if usernameEntry.get() == username and passwordEntry.get() == password:
        print("Successfully logged in")
    else:
        messagebox.showerror(title="Error", message="Failed to login.")

frame = tkinter.Frame(bg='#878787')


#Creating Widget
loginLabel = tkinter.Label(frame, text="Login", bg='#878787', fg='#FFFFFF', font=("Arial",30))
usernameLabel = tkinter.Label(frame, text="Username", bg='#878787', fg='#FFFFFF', font=("Arial",16))
usernameEntry = tkinter.Entry(frame, font=("Arial",30))
passwordLabel = tkinter.Label(frame, text="Password", bg='#878787', fg='#FFFFFF', font=("Arial",16))
passwordEntry = tkinter.Entry(frame, show="*", font=("Arial",30))
loginButton = tkinter.Button(frame, text="Login", bg='#666666', fg='#FFFFFF', font=("Arial",30), command=login)

#Placing widget on the screen
loginLabel.grid(row=0, column=0, columnspan=5, sticky="news", pady=40)
usernameLabel.grid(row=1, column=0)
usernameEntry.grid(row=1, column=1, pady=20)
passwordLabel.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1, pady=20)
loginButton.grid(row=3, column=0, columnspan=5, pady=30)

frame.pack()
# Starten Sie die GUI-Schleife
window.mainloop()
'''
def clear():
    list = window.grid_slaves()
    for i in list:
        i.destroy()

class Menu:
    def __init__(self):
        clear()
        self.Cardgame = Button(window, text="Cardgame-Nope", font("Arial", 14), command=)
'''

