## Aufbau

Die GUI befindet sich in dem Ordner src/GUI.py. Mit Hilfe der Python Bibliothek tkinter kann man schnellere und gezieltere Ergebnisse erzielen, um ein effektiveres Programmieren zu gewährleisten. Dabei ist das Script so aufgebaut das man neue Fenster nur Namentlich in die Klasse MainWindow stecken muss. `class MainWindow(tk.Tk):` Diese Schnittstelle befindet sich in der For Schleife `for F in (Login, Register, GameMenu, PlayGame, History, Tournament):` direkt innerhalb der Klasse. Diese For Schleife erwartet in den Bedingungsblock eine Klasse die ein neues `tk.Frane` erstellet und wenn das der Fall ist, packt diese die ganzen Frames in einen Container um ein schneller durch intarieren zu garantieren. 

## Methoden

Mit der `def showFrame(self, cont):` Methode kann man nach wünsch das aktuelle Sichtbare Frame ändern.

## Gui Frames
##### Login
![The San Juan Mountains are beautiful!](/assets/Login/electrocat.png)
