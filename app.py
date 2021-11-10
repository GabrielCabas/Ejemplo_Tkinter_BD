import tkinter as tk
from database import Database
from jugador import jugador
class App:#Main window
    def __init__(self, db):
        self.root = tk.Tk()
        #Algunas especificaciones de tamaño y título de la ventana
        self.root.geometry("700x400")
        self.root.title("Jugadores")
        self.jugador = jugador(self.root, db)#En un principio, muestra los jugadores
        self.root.mainloop()#Empieza a correr la interfaz
def main():
    db = Database()#Conecta a la base de datos
    App(db)#La app xD
if __name__ == "__main__":
    main()