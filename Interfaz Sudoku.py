from tkinter import *
from datetime import datetime, timedelta
from Funciones_Pryecto1_equipo2 import *

# Función para actualizar el cronómetro
def actualizar_cronometro():
    global tiempo_inicial, cronometro_corriendo
    if cronometro_corriendo:
        tiempo_actual = datetime.now()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        tiempo_formateado = str(tiempo_transcurrido).split(".")[0]  # Formatear tiempo sin microsegundos
        etiqueta_cronometro.config(text=tiempo_formateado)
        raiz.after(1000, actualizar_cronometro)  # Actualizar cada segundo

# Función para iniciar el cronómetro
def iniciar_cronometro():
    global tiempo_inicial, cronometro_corriendo
    if not cronometro_corriendo:
        tiempo_inicial = datetime.now()
        cronometro_corriendo = True
        actualizar_cronometro()

# Función para detener el cronómetro
def detener_cronometro():
    global cronometro_corriendo
    cronometro_corriendo = False

# Función para reiniciar el cronómetro
def reiniciar_cronometro():
    global tiempo_inicial, cronometro_corriendo
    tiempo_inicial = None
    cronometro_corriendo = False
    etiqueta_cronometro.config(text="00:00:00")

# Función para iniciar el juego de Sudoku con el tamaño y dificultad seleccionados
def iniciar_sudoku():
    selected_size = var_size.get()
    selected_difficulty = var_difficulty.get()
    if selected_size == "Tamaño 4x4":
        if selected_difficulty == "Dificultad Fácil":
            matriz = iniciarMatriz(4)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 8)
            dibujarTabla4x4(cuadricula, tabla)
        elif selected_difficulty == "Dificultad Intermedia":
            matriz = iniciarMatriz(4)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 10)
            dibujarTabla4x4(cuadricula, tabla)
        elif selected_difficulty == "Dificultad Difícil":
            matriz = iniciarMatriz(4)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 12)
            dibujarTabla4x4(cuadricula, tabla)
    else:
        if selected_difficulty == "Dificultad Fácil":
            matriz = iniciarMatriz(9)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 45)
            dibujarTabla9x9(cuadricula, tabla)
        elif selected_difficulty == "Dificultad Intermedia":
            matriz = iniciarMatriz(9)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 52)
            dibujarTabla9x9(cuadricula, tabla)
        elif selected_difficulty == "Dificultad Difícil":
            matriz = iniciarMatriz(9)
            matrizResuelta = resolver_sudoku(matriz)
            cuadricula = cerosRandom(matrizResuelta, 59)
            dibujarTabla9x9(cuadricula, tabla)

#Funciones para retornar resultados de los valores
def boton_nuevo_click():
    resultado = iniciar_sudoku()
    # Tratar el valor devuelto por el botón "Nuevo Juego"
    print(resultado)

def boton_borrar_click():
    # Realizar operaciones para el botón "Borrar Juego"
    print("Borrar Juego")

def boton_resolver_click():
    # Realizar operaciones para el botón "Resolver Juego"
    print("Resolver Juego")

def boton_guardar_click():
    # Realizar operaciones para el botón "Guardar Juego"
    print("Guardar Juego")

def boton_cargar_click():
    # Realizar operaciones para el botón "Cargar Juego"
    print("Cargar Juego")

def boton_introduccion_click():
    # Realizar operaciones para el botón "Introducción"
    print("Introducción")

# --------------------------------------------------------------------- Sudoku Funciones ----------------------------------------------

def iniciarMatriz(n):
    if n == 4:
        cuadricula = crearMatriz4x4()
    elif n == 9:
        cuadricula = crearMatriz9x9()
    return cuadricula

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


"=================================================Interfaz gráfica====================================================================================="
raiz = Tk()
raiz.title("Sudoku")
raiz.geometry("900x350")

tabla = Frame(raiz)
tabla.grid(row=2, column=5)

# Ancho fijo para todos los botones
#boton_width = 20

# Color de fondo gris
boton_bg_color = "gray"

#Fuente de la interfaz
fuente = ("Arial", 12)

# Etiqueta para "Controles"
controles = Label(raiz, bg="deep sky blue", text="Controles",width=21,font=fuente)
controles.grid(row=1, column=2,sticky="nw")

# Etiqueta para "Sudoku"
sudoku = Label(raiz, bg="deep sky blue", text="Sudoku", width=60,font=fuente)
sudoku.grid(row=1, column=4, columnspan=3)

# Lista de tamaños de Sudoku disponibles
tamanos_sudoku = ["Tamaño 4x4", "Tamaño 9x9"]
var_size = StringVar()
var_size.set("Tamaño 4x4")  # Valor predeterminado

# Menú desplegable para seleccionar el tamaño del Sudoku
opcion_tamano = OptionMenu(raiz, var_size, *tamanos_sudoku)
opcion_tamano.config(width=17,bg=boton_bg_color,font=fuente)  # Establecer el ancho igual al de los botones
opcion_tamano.grid(row=2, column=2,sticky="nw")

# Lista de dificultades
dificultades = ["Dificultad Fácil", "Dificultad Intermedia", "Dificultad Difícil"]
var_difficulty = StringVar()
var_difficulty.set("Dificultad Fácil")  # Valor predeterminado

# Menú desplegable para seleccionar la dificultad
opcion_dificultad = OptionMenu(raiz, var_difficulty, *dificultades)
opcion_dificultad.config(width=17,bg=boton_bg_color,font=fuente)  # Establecer el ancho igual al de los botones
opcion_dificultad.grid(row=4, column=2,sticky="nw")


# Botón para nuevo juego de Sudoku con el tamaño y dificultad seleccionados
boton_nuevo = Button(raiz, text="Nuevo Juego", command=boton_nuevo_click, width=20, bg=boton_bg_color,font=fuente)
boton_nuevo.grid(row=5, column=2,sticky="nw")

# Botón para borrar el juego
boton_borrar = Button(raiz, text="Borrar Juego", command=boton_borrar_click, width=20, bg=boton_bg_color,font=fuente)
boton_borrar.grid(row=6, column=2,sticky="nw")

# Botón para resolver el juego
boton_resolver = Button(raiz, text="Resolver Juego", command=boton_resolver_click, width=20, bg=boton_bg_color,font=fuente)
boton_resolver.grid(row=7, column=2,sticky="nw")

# Botón para guardar el juego
boton_guardar = Button(raiz, text="Guardar Juego", command=boton_guardar_click, width=20, bg=boton_bg_color,font=fuente)
boton_guardar.grid(row=8, column=2,sticky="nw")

# Botón para cargar el juego
boton_cargar = Button(raiz, text="Cargar Juego", command=boton_cargar_click, width=20, bg=boton_bg_color,font=fuente)
boton_cargar.grid(row=9, column=2,sticky="nw")

# Botón para mostrar la introducción
boton_introduccion = Button(raiz, text="Introducción", command=boton_introduccion_click, width=20, bg=boton_bg_color,font=fuente)
boton_introduccion.grid(row=10, column=2,sticky="nw")

# Etiqueta para el cronómetro
etiqueta_cronometro = Label(raiz,bg="deep sky blue",font=fuente, width=21, text="00:00:00")
etiqueta_cronometro.grid(row=12, column=2,sticky="nw")

# Botones para controlar el cronómetro
boton_iniciar_cronometro = Button(raiz,width=7,bg=boton_bg_color,font=fuente, text="Iniciar", command=iniciar_cronometro)
boton_iniciar_cronometro.grid(row=13, column=1,sticky="nw")

boton_detener_cronometro = Button(raiz,width=8,bg=boton_bg_color ,font=fuente, text="Detener", command=detener_cronometro)
boton_detener_cronometro.grid(row=13, column=2,sticky="nw")

boton_reiniciar_cronometro = Button(raiz,width=7,bg=boton_bg_color,font=fuente,text="Reiniciar", command=reiniciar_cronometro)
boton_reiniciar_cronometro.grid(row=13, column=3,sticky="nw")

# Inicializar variables del cronómetro
tiempo_inicial = None
cronometro_corriendo = False

raiz.mainloop()