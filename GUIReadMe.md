## Aufbau

Die GUI befindet sich in dem Ordner src/GUI.py. Mit Hilfe der Python Bibliothek tkinter kann man schnellere und gezieltere Ergebnisse erzielen, um ein effektiveres Programmieren zu gewährleisten. Dabei ist das Script so aufgebaut das man neue Fenster nur Namentlich in die Klasse MainWindow stecken muss. `class MainWindow(tk.Tk):` Diese Schnittstelle befindet sich in der For Schleife `for F in (Login, Register, GameMenu, PlayGame, History, Tournament):` direkt innerhalb der Klasse. Diese For Schleife erwartet in den Bedingungsblock eine Klasse die ein neues `tk.Frane` erstellet und wenn das der Fall ist, packt diese die ganzen Frames in einen Container um ein schneller durch intarieren zu garantieren. 

## Methoden

Mit der `def showFrame(self, cont):` Methode kann man nach wünsch das aktuelle Sichtbare Frame ändern.

## Gui Frames
#### Login
![Login!](/assets/GuiLogin.PNG)

Dieses Fenster wird als erstes bei dem Programmstart geöffnet. Dabei kann man sich mit seinem Account verbinden oder über den Register Knopf sich neu registrieren. Für die Sicherheitsaspekte wird das Eingabefeld beim Password mit "*" Zensiert

#### Registrierung

![Login!](/assets/Register.png)

Wie auch schon bei dem Login Fenster muss man hier auch seinen Benutzernamen und ein Password wählen. Zudem kommt aber auch noch, das man sein Vornamen und Nachnamen angeben muss um erfolgreich sich zu Registrieren.

#### Menü

![Menü!](/assets/GameMenu.png)

Wenn man sich dann erfolgreich eingeloggt hat, kommt man in den Hauptbildschirm von dem Spiel. Dabei hat man zur Auswahl das man ein Spiel spielen will, seine letzen Spiele anschauen will, ein Turnier spielen und in den Login Screen zurück gehen

#### Play

![Menü!](/assets/Play.png)

#### History

![Menü!](/assets/History.png)

#### Turnier

![Menü!](/assets/Tournament.png)

In diesem Fenster kann man sich mit eine vorhandenes Tunier verbinden über den Join Knof, ein neues Tunier stellen mit Create und das Tunier verlassen über Leave. Mit dem Button Back to Menu kommt man dann wieder in das Menü
