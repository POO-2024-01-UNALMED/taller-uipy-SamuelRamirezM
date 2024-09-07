from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=500, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "1"))
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "2"))
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "3"))
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "4"))
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "5"))
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "6"))
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "7"))
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "8"))
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "9"))
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command = lambda: calcularResultado(1))
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command = lambda: ingresarSimbolo(1, "."))
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "+"))
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "-"))
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "*"))
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command = lambda: ingresarSimbolo(1, "/"))
boton_division.grid(row=4, column=3, padx=1, pady=1)

# Configuración eventos.

# Varibles para los numeros y el resultado.
numero1 = 0
numero2 = 0
resultado = 0

# Método para insertar un número u operador en la pantalla.
def ingresarSimbolo(event, simbolo):
    mostrado = pantalla.get()
    pantalla.delete(0, "end")
    pantalla.insert(0, mostrado + simbolo)

# Calcular y mostrar el resultado al presionar el boton "=" (igual).
def calcularResultado(event):
    global numero1, numero2, resultado
    mostrado = pantalla.get()
    if "+" in mostrado:
        listaNumeros = mostrado.split("+")
        numero1 = listaNumeros[0]
        numero2 = listaNumeros[1]
        resultado = float(numero1) + float(numero2)
    elif "-" in mostrado:
        listaNumeros = mostrado.split("-")
        numero1 = listaNumeros[0]
        numero2 = listaNumeros[1]
        resultado = float(numero1) - float(numero2)
    elif "*" in mostrado:
        listaNumeros = mostrado.split("*")
        numero1 = listaNumeros[0]
        numero2 = listaNumeros[1]
        resultado = float(numero1) * float(numero2)
    elif "/" in mostrado:
        listaNumeros = mostrado.split("/")
        numero1 = listaNumeros[0]
        numero2 = listaNumeros[1]
        resultado = float(numero1) / float(numero2)

    pantalla.delete(0, "end")
    pantalla.insert(0, str(resultado))

root.mainloop()