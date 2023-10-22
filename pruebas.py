from tkinter import *
from Funciones_Pryecto1_equipo2 import *

botonesSudoku = []
def colorCuadrantes9x9(i, j): # Colores que diferencian cada cuadrante en el sudoku
    colores = ["lightgray", "sky blue"]
    return colores[(i // 3 + j // 3) % 2]

def colorCuadrantes4x4(i, j): # Colores que diferencian cada cuadrante en el sudoku
    colores = ["lightgray", "sky blue"]
    return colores[(i // 2 + j // 2) % 2]

def dibujarTabla9x9(cuadricula, tabla):
    global botonesSudoku
    for i in range(9):
        filaBotones = []
        for j in range(9):
            valorCelda = cuadricula[i][j]
            colorCelda = colorCuadrantes9x9(i, j)

            def colocarValores(valor, fila, columna):
                return lambda: presionarBoton9x9(valor, fila, columna)

            if valorCelda != 0:
                boton = Button(tabla, text=str(valorCelda), width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(valorCelda, i, j))
            else:
                boton = Button(tabla, width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(None, i, j))
            boton.grid(row=i, column=j, sticky=E)
            filaBotones.append(boton)

        botonesSudoku.append(filaBotones)

def dibujarTabla4x4(cuadricula, tabla):
    global botonesSudoku
    for i in range(4):
        filaBotones = []
        for j in range(4):
            valorCelda = cuadricula[i][j]
            colorCelda = colorCuadrantes4x4(i, j)

            def colocarValores(valor, fila, columna):
                return lambda: presionarBoton4x4(valor, fila, columna)

            if valorCelda != 0:
                boton = Button(tabla, text=str(valorCelda), width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(valorCelda, i, j))
            else:
                boton = Button(tabla, width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(None, i, j))
            boton.grid(row=i, column=j, sticky=E)
            filaBotones.append(boton)

        botonesSudoku.append(filaBotones)

def presionarBoton9x9(valor, fila, columna):
    print(f"Click boton, tiene un valor de: {valor} en la fila: {fila} y columna: {columna}")

    for i in range(9): # Quitar el resalto de los botones
        for j in range(9):
            if (i, j) != (fila, columna):
                botonesSudoku[i][j].config(bg=colorCuadrantes9x9(i, j))

    for i in range(9): # Resaltar la fila
        botonesSudoku[i][columna].config(bg="lightyellow")

    for j in range(9): # Resaltar la columna
        botonesSudoku[fila][j].config(bg="lightyellow")

    # regiones
    inicioFilaCuadrante = (fila // 3) * 3
    inicioColumnaCuadrante = (columna // 3) * 3
    finalFilaCuadrante = inicioFilaCuadrante + 3
    finalColumnaCuadrante = inicioColumnaCuadrante + 3

    for i in range(inicioFilaCuadrante, finalFilaCuadrante): # Resaltar cuadrante
        for j in range(inicioColumnaCuadrante, finalColumnaCuadrante):
            botonesSudoku[i][j].config(bg="lightyellow")

    botonesSudoku[fila][columna].config(bg="yellow") # Resaltar celda

def presionarBoton4x4(valor, fila, columna):
    print(f"Click boton, tiene un valor de: {valor} en la fila: {fila} y columna: {columna}")

    for i in range(4): # Quitar el resalto de los botones
        for j in range(4):
            if (i, j) != (fila, columna):
                botonesSudoku[i][j].config(bg=colorCuadrantes9x9(i, j))

    for i in range(4): # Resaltar la fila
        botonesSudoku[i][columna].config(bg="lightyellow")

    for j in range(4): # Resaltar la columna
        botonesSudoku[fila][j].config(bg="lightyellow")

    # regiones
    inicioFilaCuadrante = (fila // 2) * 2
    inicioColumnaCuadrante = (columna // 2) * 2
    finalFilaCuadrante = inicioFilaCuadrante + 2
    finalColumnaCuadrante = inicioColumnaCuadrante + 2

    for i in range(inicioFilaCuadrante, finalFilaCuadrante): # Resaltar cuadrante
        for j in range(inicioColumnaCuadrante, finalColumnaCuadrante):
            botonesSudoku[i][j].config(bg="lightyellow")

    botonesSudoku[fila][columna].config(bg="yellow") # Resaltar celda

# Example usage:
root = Tk()
matriz = crearMatriz9x9()
matrizResuelta = resolver_sudoku(matriz)
cuadricula = cerosRandom(matrizResuelta, 45)

tabla = Frame(root)
tabla.grid(row=2, column=4)

dibujarTabla9x9(cuadricula, tabla)

#dibujarTabla4x4(cuadricula, tabla)

root.mainloop()








