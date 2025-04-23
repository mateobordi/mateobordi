import tkinter as tk

def main():
    ventana = tk.Tk()
    ventana.title("Ejercicio 2")
    ventana.geometry("700x700")
    ventana.configure(bg="light blue")

    etiqueta = tk.Label (ventana, text="Ejercicio 2", font=("arial",16))
    etiqueta.pack()

    etiqueta = tk.Label (ventana, text="mateo bordi", font=("arial",16))
    etiqueta.pack()
if __name__=="__main__":
    mani()                    
  
