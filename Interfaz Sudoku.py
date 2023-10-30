from tkinter import *
from datetime import datetime, timedelta
from Funciones_Pryecto1_equipo2 import *
import pickle
from tkinter import messagebox
from copy import copy, deepcopy

global cuadricula
global cuadricula_original
cuadricula_original = []
cuadricula = []


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
    global cuadricula 
    global matrizResuelta
    global cuadricula_original
    
    
    global tabla
    tabla.destroy() # limpia el frame para borrar los botones anteriores
    tabla = Frame(raiz)
    tabla.place(x=310, y=30)

    global botonesSudoku
    botonesSudoku = [] #limpia los botones para generarlos nuevamente

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

    cuadricula_original = deepcopy(cuadricula)

#Funciones para retornar resultados de los valores
def boton_nuevo_click():
    resultado = iniciar_sudoku() # Tratar el valor devuelto por el botón "Nuevo Juego"
    

"""
Función Botón de borrar
Reestableces la cuadricula del juego al estado original en el que se inicio la partida.
Entrada: No tiene parámetros.
Restricciones: El tamaño de las tablas deben ser de 4 o 9.
Salida: No retorna un valor pero limpia y recrea el frame del juego.
"""
def boton_borrar_click():
    global cuadricula_original, cuadricula #declara las instancias globales a utilizar 
    global tabla
    global botonesSudoku #permite manipular la lista global de botones relacionados a el sudoku
    
    tabla.destroy() #limpia el frame para borrar los botones anteriores
    tabla = Frame(raiz) #crear el nuevo frame del objeto y lo asigna a ña variable tabla
    tabla.place(x=310, y=30) #posición del frame desntro de la raíz (el contenedor)

    botonesSudoku = [] #limpia los botones para generarlos nuevamente
    cuadricula = deepcopy(cuadricula_original) #hace un deepcopy para trabajar con este y no con una copia normal

    if len(cuadricula) == 4: # verifica las longitudes de las cuadriculas
        dibujarTabla4x4(cuadricula, tabla) #Si la condición aesverdadera llama a la función
    elif len(cuadricula) == 9:
        dibujarTabla9x9(cuadricula, tabla)

    print("Juego Borrado") #imprime el mensaje "Juego Borrado" en la consola


"""
Función Botón resolver Sudoku
Se encarga de mostrar la solución al usuario de esa partida.
Entrada: No tiene parámetros.
Restricciones: El tamaño de las tablas deben ser de 4 o 9.
Salida: No retorna un valor.
"""
def boton_resolver_click():
    global matrizResuelta  #declara las instancias globales a utilizar 
    global tabla
    global botonesSudoku
    global cuadricula_original
    
    tabla.destroy() # limpia el frame para borrar los botones anteriores
    tabla = Frame(raiz)  #crear el nuevo frame del objeto y lo asigna a ña variable tabla
    tabla.place(x=310, y=30)  #posición del frame desntro de la raíz (el contenedor)

    botonesSudoku = [] #limpia los botones para generarlos nuevamente
    cuadricula = deepcopy(cuadricula_original)

    if len(matrizResuelta) == 4:  # verifica las longitudes de las cuadriculas
        dibujarTabla4x4(matrizResuelta, tabla)
    elif len(matrizResuelta) == 9:
        dibujarTabla9x9(matrizResuelta, tabla)

    print("Guardar Juego") #imprime el mensaje "Guardar Juego" en la consola



def guardar_partida():
    global cuadricula
    try:
        # Abre un archivo en modo escritura binaria
        with open("partida_sudoku.pkl", "wb") as archivo:
            # Crea un diccionario con los datos de la partida a guardar
            datos_partida = {
                "cuadricula": cuadricula,  # Guarda la cuadrícula del juego
                "matrizResuelta": matrizResuelta  # Guarda la matriz resuelta del juego
            }
            # Utiliza la biblioteca "pickle" para escribir los datos del diccionario en el archivo
            pickle.dump(datos_partida, archivo)
        # Muestra un mensaje de éxito en la consola
        print("Partida guardada con éxito.")
    except Exception as e:
        # En caso de un error al guardar la partida, muestra un mensaje de error en la consola
        print(f"Error al guardar la partida: {str(e)}")

# Función para cargar una partida de Sudoku desde un archivo binario
def cargar_partida():
    global cuadricula, matrizResuelta
    try:
        # Abre un archivo en modo lectura binaria
        with open("partida_sudoku.pkl", "rb") as archivo:
            # Carga los datos de la partida desde el archivo
            datos_partida = pickle.load(archivo)
            cuadricula = datos_partida["cuadricula"]  # Actualiza la cuadrícula con los datos cargados
            matrizResuelta = datos_partida["matrizResuelta"]  # Actualiza la matriz resuelta con los datos cargados
        # Muestra un mensaje de éxito en la consola
        print("Partida cargada con éxito.")
        # Actualiza la interfaz gráfica para reflejar la partida cargada
        if len(cuadricula) == 4:
            dibujarTabla4x4(cuadricula, tabla)  # Llama a una función para dibujar un tablero de 4x4
        elif len(cuadricula) == 9:
            dibujarTabla9x9(cuadricula, tabla)  # Llama a una función para dibujar un tablero de 9x9
    except Exception as e:
        # En caso de un error al cargar la partida, muestra un mensaje de error en la consola
        print(f"Error al cargar la partida: {str(e)}")    

"""
Función Botón Introducción
Muestra un cuadro con las instrucciones para jugar Sudoku.
Entrada: No tiene parámetros.
Restricciones: Depende de la biblioteca messagebox de tkinter
Salida: No retorna un valor.
"""
def boton_introduccion_click():
    messagebox.showinfo("Introducción", "Bienvenido al sudoku") #muestra un cuadro con la infomación suministrada, modúlo de tkinter


"""
Función Partida ganada
Muestra un cuadro con el mensaje de felicitación si el usuario ganó la partida de Sudoku.
Entrada: No tiene parámetros.
Restricciones: Depende de la biblioteca messagebox de tkinter
Salida: No retorna un valor.
"""
def partida_ganada(cuadricula): 
    if matrizLlena(cuadricula):  # Comprueba si todos los espacios están llenos y correctos
        messagebox.showinfo("¡Felicidades!", "Has ganado la partida")  #muestra un cuadro con la infomación suministrada, modúlo de tkinter


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

    agregarBotonesNumeros(9)

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
                # Se usa el textVairiable para hacer que los botones queden estaticos y no cambien al encontrar el correcto.
                boton = Button(tabla, text=str(valorCelda),  textvariable=str(valorCelda), width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(valorCelda, i, j))
            else:
                boton = Button(tabla, width=4, height=2, font=("Arial", 16), bg=colorCelda, command=colocarValores(None, i, j))
            boton.grid(row=i, column=j, sticky=E)
            filaBotones.append(boton)

        botonesSudoku.append(filaBotones)

    agregarBotonesNumeros(4) 

def agregarBotonesNumeros(size):
    global botonesSudoku

    def funcionAgregar(valor):
        return lambda: agregarValor(valor)
    
    filaBotones = []
    for i in range(size):

        labelEspaciador = Label(tabla, height=1, text="",width=3,font=fuente)
        labelEspaciador.grid(row=size, column=i, sticky=N)
        boton = Button(tabla, text=str(i+1), width=3, height=1, font=("Arial", 16), bg="lightgray", command=funcionAgregar(i+1))
        boton.grid(row=size+1, column=i, sticky=N)
        filaBotones.append(labelEspaciador)
        filaBotones.append(boton)

    botonesSudoku.append(filaBotones)


"""
Función Agregar Valor al sudoku
Se encarga de agregar un valor numeral a un botón, comprando si el valor es correcto y actualiza valor al color verde, de lo contrario al color rojo en la interfaz.
Entrada: Valor númerivo que el usuario agrega al sudoku.
Restricciones: Valor entero positivo del 1 al 9.
Salida: No retorna un valor.
"""
def agregarValor(valor): #se declaran las variables necesarias para la función
    global cuadricula
    global matrizResuelta
    global filaSelecionada
    global columnaSelecionada

    if botonesSudoku[filaSelecionada][columnaSelecionada].cget("textvariable") == "": #verifica las posiciones de fila y columna selecionada del arreglo botonesSudoku para saber si tiene un valor vacío .
        jugadaCorrecta = guardarJugada(cuadricula, matrizResuelta, filaSelecionada+1, columnaSelecionada+1, valor) #indica si la jugada es correcta o no y se guarda en jugadaCorrecta       

        if jugadaCorrecta: #entonces si es correcta 
            botonesSudoku[filaSelecionada][columnaSelecionada].config(text=valor, textvariable=valor, bg="#00C957", fg="#d1220a") #se muestra el valor con fondo verde y el número rojo.
            partida_ganada(cuadricula) # verifica si con la juagada se a ganado el sudoku 
            
        else: #si no es correcta
            botonesSudoku[filaSelecionada][columnaSelecionada].config(text=valor, bg="#ff4c33", fg="#d1220a") #se miestra el valor con fondo rojo y el número rojo oscuro. 

        guardarHistorial(filaSelecionada, columnaSelecionada, valor, jugadaCorrecta) #ya verificadas las jugadas se guarda en el hsitorial
    else: #si ya se tiene un valor
        print("La casilla en la fila " + str(filaSelecionada) + " y en la columna " + str(columnaSelecionada) + " ya tiene un valor") #si no se imprime un mensaje que ya hay un valor e la fila y columna respectiva

"""
Función Historial guardado
Guarda la información de la fila, columna y valor ingresado por el usuario en una partida.
Verifica si la jugada ingresada es correcta o no y da un mensaje.
Entrada: Un número entero para fila, columna, valor ingresado y un booleano que indica sí es jugadaCorrecta o no.
Restricciones: Fila, columna y valor deben ser enteros positivos y jugadaCorrecta un booleano.
Salida: No retorna un valor pero modifica la variable "historial".
"""
def guardarHistorial(fila, columna, valor, jugadaCorrecta): 
    global historial #la definimos global para poder modificarla dentro de esta función	

    mensajeJusgadaCorrecta = "" #inicializar
    if jugadaCorrecta: #si el número en jugada correcta es correcto tira el mensaje de lo contrario dice que es incorrecto.
        mensajeJusgadaCorrecta = "El valor ingresado es correcto"
    else:
        mensajeJusgadaCorrecta = "El valor ingresado es incorrecto"

    # Se agrega al historial de la jugada y se imprime la infomación de si la posición, el valor ingresado es correcto o no. 
    historial.append("\nEn la casilla de la fila -> " + str(fila+1) + " y de la columna -> " + str(columna+1) + "\nSe ingresó el valor " + str(valor) + ". \n" + mensajeJusgadaCorrecta)
    print(historial[-1])  #imprime el ultimo mensaje que se agregó al historial.




def presionarBoton9x9(valor, fila, columna):
    global filaSelecionada
    global columnaSelecionada

    
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

    filaSelecionada = fila
    columnaSelecionada = columna

def presionarBoton4x4(valor, fila, columna):
    global filaSelecionada
    global columnaSelecionada

    

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
    
    filaSelecionada = fila
    columnaSelecionada = columna


"=================================================Interfaz gráfica====================================================================================="
raiz = Tk()
raiz.title("Sudoku")
raiz.geometry("900x750")

tabla = Frame(raiz)
tabla.place(x=310, y=30)

# Ancho fijo para todos los botones
#boton_width = 20

# Color de fondo gris
boton_bg_color = "gray"

#Fuente de la interfaz
fuente = ("Arial", 12)

# Etiqueta para "Controles"
controles = Label(raiz, bg="deep sky blue", text="Controles",width=21,font=fuente)
controles.place(x=30, y=0)

# Etiqueta para "Sudoku"
sudoku = Label(raiz, bg="deep sky blue", text="Sudoku", width=60,font=fuente)
sudoku.place(x=300, y=0)
# sudoku.grid(row=1, column=4, columnspan=3)

# Lista de tamaños de Sudoku disponibles
tamanos_sudoku = ["Tamaño 4x4", "Tamaño 9x9"]
var_size = StringVar()
var_size.set("Tamaño 4x4")  # Valor predeterminado

# Menú desplegable para seleccionar el tamaño del Sudoku
opcion_tamano = OptionMenu(raiz, var_size, *tamanos_sudoku)
opcion_tamano.config(width=17,bg=boton_bg_color,font=fuente)  # Establecer el ancho igual al de los botones
opcion_tamano.place(x=28, y=25)

# Lista de dificultades
dificultades = ["Dificultad Fácil", "Dificultad Intermedia", "Dificultad Difícil"]
var_difficulty = StringVar()
var_difficulty.set("Dificultad Fácil")  # Valor predeterminado

# Menú desplegable para seleccionar la dificultad
opcion_dificultad = OptionMenu(raiz, var_difficulty, *dificultades)
opcion_dificultad.config(width=17,bg=boton_bg_color,font=fuente)
opcion_dificultad.place(x=28, y=55)  # Establecer el ancho igual al de los botones


# Botón para nuevo juego de Sudoku con el tamaño y dificultad seleccionados
boton_nuevo = Button(raiz, text="Nuevo Juego", command=boton_nuevo_click, width=20, bg=boton_bg_color,font=fuente)
boton_nuevo.place(x=30, y=90)

# Botón para borrar el juego
boton_borrar = Button(raiz, text="Borrar Juego", command=boton_borrar_click, width=20, bg=boton_bg_color,font=fuente)
boton_borrar.place(x=30, y=125)
# boton_borrar.grid(row=6, column=2,sticky="nw")

# Botón para resolver el juego
boton_resolver = Button(raiz, text="Resolver Juego", command=boton_resolver_click, width=20, bg=boton_bg_color,font=fuente)
boton_resolver.place(x=30, y=160)

# Botón para guardar el juego
boton_guardar = Button(raiz, text="Guardar Juego", command=guardar_partida, width=20, bg=boton_bg_color,font=fuente)
boton_guardar.place(x=30, y=195)

# Botón para cargar el juego
boton_cargar = Button(raiz, text="Cargar Juego", command=cargar_partida, width=20, bg=boton_bg_color,font=fuente)
boton_cargar.place(x=30, y=230)

# Botón para mostrar la introducción
boton_introduccion = Button(raiz, text="Introducción", command=boton_introduccion_click, width=20, bg=boton_bg_color,font=fuente)
boton_introduccion.place(x=30, y=265)

# Etiqueta para el cronómetro
etiqueta_cronometro = Label(raiz,bg="deep sky blue",font=fuente, width=21, text="00:00:00")
etiqueta_cronometro.place(x=30, y=300)

# Botones para controlar el cronómetro
boton_iniciar_cronometro = Button(raiz,width=7,bg=boton_bg_color,font=fuente, text="Iniciar", command=iniciar_cronometro)
boton_iniciar_cronometro.place(x=30, y=330)

boton_detener_cronometro = Button(raiz,width=8,bg=boton_bg_color ,font=fuente, text="Detener", command=detener_cronometro)
boton_detener_cronometro.place(x=105, y=330)

boton_reiniciar_cronometro = Button(raiz,width=7,bg=boton_bg_color,font=fuente,text="Reiniciar", command=reiniciar_cronometro)
boton_reiniciar_cronometro.place(x=189, y=330)

# Inicializar variables del cronómetro
tiempo_inicial = None
cronometro_corriendo = False

# Inicializar fila y columna seleccionada
filaSelecionada = 0
columnaSelecionada = 0

# Inicializar matrices
cuadricula = []
matrizResuelta = []

#Inicializar el Historial 
historial = []

raiz.mainloop()

