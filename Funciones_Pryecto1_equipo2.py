import random
import copy
"""
Jose Matamoros
Mariana Torres
Amanda Ramirez
"""
"=======================================Funciones para que las funciones fundamentales sirvan============================================================"

#Toma como entrada una matriz y devuelve sus indices i,j como tuplas en forma de lista para evaluar los indices asociados
def estructura(matriz):  
    tamaño = len(matriz[0])
    opciones = [-1 if matriz[i][j] else 1
                for i in range(tamaño)
                for j in range(tamaño)]
   
    return matriz, tamaño, opciones, 0, 0

#Toma una matriz cuadrada y la estructura en forma de filas y columnas
def formarRegion(matriz):        
    tamano = 3 if len(matriz) == 9 else 2 #define la cantidad horizontal de cuadrantes que tenemos 
    resultado = ""
    
    for fila in range(len(matriz)):       
        if fila % tamano == 0 and fila != 0:
            resultado += "- " * int((tamano * tamano)+(len(matriz)/tamano)-1) + "\n" # separa con línea de guiones para separar las regiones

        for columna in range(len(matriz[fila])):           
            if columna % tamano == 0 and columna != 0:
                resultado += "| " # Para separar las regiones
            resultado += str(matriz[fila][columna]) + " "
        
        resultado += "\n"

    return resultado

#Realisa una una linea para separar diferenciar las matrices
def imprimirMatriz(matriz):
    print(formarRegion(matriz))
    print("")
    print('===========================')

#Verifica si un número n está presente en la fila y de la matriz
def fila(matriz, n, y): 
    return n in matriz[y]

#Verifica si un número n está presente en la columna x de la matriz
def columna(matriz, n, x): 
    if len(matriz) == 4:
        if 0 <= x < 4:  
            return n in [matriz[_][x] for _ in range(4)]
        else:
            raise ValueError("El valor de 'x' está fuera de los límites válidos para una matriz 4x4.")
    elif len(matriz) == 9:
        if 0 <= x < 9:  
            return n in [matriz[_][x] for _ in range(9)]
        else:
            raise ValueError("El valor de 'x' está fuera de los límites válidos para una matriz 9x9.")

#Verifica si un número n está en la región a la que pertenece la celda (x, y) de la matriz
def region(matriz, n, x, y): 
    if len(matriz)==9:
        return n in [matriz[b][a] for a in range(x//3*3, x//3*3+3) for b in range(y//3*3, y//3*3+3)]
    elif len(matriz)==4:
        return n in [matriz[b][a] for a in range(x//2*2, x//2*2+2) for b in range(y//2*2, y//2*2+2)]

#Verifica si un número n es válido en la posición (x, y) de la matriz según las reglas del Sudoku
def verificacionCompleta(matriz, n, x, y): 
    if fila(matriz, n, y) or columna(matriz, n, x) or region(matriz, n, x, y):
        return True
    else:
        return False

#Retrocede en la matriz desde la posición (x, y) para encontrar la próxima celda editable además actualiza la posición (x, y) y devuelve las nuevas coordenadas    
def revisar(matriz, x, y, opciones):
    if len(matriz) == 9: #Verifica si la matiz es 9x9
        matriz[y][x] = 0 #Reasigna la entrada y le da valor de 9
        opciones[y * 9 + x] = 1 #Determina que esta posicion está libre
        if x == 0:
            x = 8
            y -= 1
        else:
            x -= 1

        while opciones[y * 9 + x] == -1: #mientras la opción en la posición y * 9 + x es igual a -1, lo que indica que esa posición ya se ha intentado anteriormente y no es válida.
            if x == 0:
                x = 8
                y -= 1 #Nuevamente se verifica si x es igual a 0 y, si es así, se retrocede una fila y se coloca x en 8 para moverse a la última columna de la fila anterior
            else:
                x -= 1 #Si x no es igual a 0, simplemente se reduce en 1 para retroceder una columna en la misma fila

        return x, y #(x, y) actualizadas después de retroceder en la resolución del Sudoku
    
    elif len(matriz) == 4: # tiene la misma lógica solo que para matrices 4x4
        matriz[x][y] = 0
        opciones[x * 4 + y] = -1
        if x == 0:
            x = 3
            y -= 1
        else:
            x -= 1

        while opciones[y * 4 + x] == -1:
            if x == 0:
                x = 3
                y -= 1
            else:
                x -= 1

        return x, y

#Esta función verifica si la matriz está completa y llena correctamente
def comprobacion(matriz): #determina si el sudoku esta completo y lleno correctamente
    for fila in matriz:
        if 0 in fila:
            return False

    return True

#Esta función avanza a la siguiente celda en una matriz 9x9 desde la posición (x, y)
def continuar9x9(x, y): 
        if x == 8:
            x = 0
            y += 1
        else:
            x += 1

        return x, y

#Esta función avanza a la siguiente celda en una matriz 4x4 desde la posición (x, y)
def continuar4x4(x, y): 
        if x == 3:
            x = 0
            y += 1
        else:
            x += 1

        return x, y

#Esta función intenta convertir una entrada en un entero y maneja cualquier error si la entrada no es válida
def validarEntradaEntera(x):
    try:
        return int(x)
    except:
        raise TypeError("\nSolo valores enteros son permitidos\n")    

#Esta función verifica si un número está dentro de un rango especificado y lanza una excepción si está fuera de ese rango.
def validarNumeroEnRango(x, rangoInferior, rangoSuperior):    
    if x < rangoInferior or x > rangoSuperior:
        raise Exception("\nSolo valores enteros entre " + str(rangoInferior) + " y " + str(rangoSuperior) + " son permitidos\n")
    return True



"=======================================Funciones fundamentales ============================================================"

#===============================crea un matriz 9x9 llena de 0=============================================
def crearMatriz9x9(): #crea una matriz 9x9 llena de 0's
    matriz = [[0 for _ in range(9)] for _ in range(9)]
    return matriz

#===============================crea un matriz 4x4 llena de 0=============================================
def crearMatriz4x4(): #crea una matriz 4x4 llena de 0's
    matriz = [[0 for _ in range(4)] for _ in range(4)]
    return matriz

#=========Se encarga de dar una solucion a la matriz con las restricciones que necesita un sudoku======
def resolver_sudoku(matriz):
    if len(matriz)==9: #verifica si la matriz es de tamaño 9x9
        matriz, tamaño, opciones, x, y = estructura(matriz)#llama a la función estructura(matriz) para obtener información inicial sobre la matriz y se desempaqueta en las variables matriz, tamaño, opciones, x, e y.
        
        while not comprobacion(matriz): #La función comprobacion(matriz) se utiliza para verificar si la matriz está completa y llena correctamente.
            c = y * tamaño + x #Se calcula un índice c en función de las coordenadas (x, y) y el tamaño de la matriz. Este índice se utiliza para acceder a las opciones disponibles en la lista opciones.
            if opciones[c] != -1:
                if verificacionCompleta(matriz, opciones[c], x, y): #Se llama a la función verificacionCompleta(matriz, opciones[c], x, y) para verificar si colocar la opción actual en la posición (x, y) es válido
                    if opciones[c] != 9:
                        opciones[c] += 1
                        continue
                    else:
                        x, y = revisar(matriz, x, y, opciones) #revisar(matriz, x, y, opciones) para retroceder a la posición anterior donde se puede hacer un cambio válido en la matriz
                else:
                    matriz[y][x] = opciones[c]
                    x, y = continuar9x9(x, y)
            else:
                x, y = continuar9x9(x, y)

        return matriz #Cuando la matriz está completamente resuelta, se devuelve la matriz resuelta
    
    elif len(matriz)==4: #Tiene una lógica paracida a la a la parte anterior solo que oara un juego de 4x4
        matriz, tamaño, opciones, x, y = estructura(matriz)
        
        while not comprobacion(matriz):
            c = y * tamaño + x
            if opciones[c] != -1:
                if verificacionCompleta(matriz, opciones[c], x, y):
                    if opciones[c] != 4:
                        opciones[c] += 1
                        continue
                    else:
                        x, y = revisar(matriz, x, y, opciones)
                else:
                    matriz[y][x] = opciones[c]
                    x, y = continuar4x4(x, y)
            else:
                x, y = continuar4x4(x, y)

        return matriz


#==========Llena aleatoriamente un cuandrante de cualquier funcion 9x9==========
def llenarCuadranteAleatorio9x9(matriz):
    if len(matriz) != 9 or any(len(fila) != 9 for fila in matriz): #verifica que la matriz sea de tamaño 9x9
        raise ValueError("La matriz no es de tamaño 9x9.")
    cuadrante_fila = random.randint(0, 2) * 3 #Esta linea y la de abajo generan de manera aleatoria las coordenadas de la esquina superior izquierda de uno de los nueve cuadrantes de 3x3 en el tablero 9x9
    cuadrante_columna = random.randint(0, 2) * 3
    numeros = list(range(1, 10))
    random.shuffle(numeros)
    for i in range(3):
        for j in range(3):
            matriz[cuadrante_fila + i][cuadrante_columna + j] = numeros.pop() #Se utiliza un bucle anidado para recorrer las filas y columnas de un cuadrante de 3x3. En cada iteración, se toma un número de la lista numeros  y se coloca en la matriz en la posición correspondiente al cuadrante.
    return matriz

#==========Llena aleatoriamente un cuandrante de cualquier funcion 4x4==========
def llenarCuadranteAleatorio4x4(matriz): #Tiene una lógica pareciada a la anterior solo que con matrices 4x4
    if len(matriz) != 4 or any(len(fila) != 4 for fila in matriz):
        print("La matriz no es de tamaño 4x4.")
        return
    cuadrante_fila = random.randint(0, 1) * 2  # Elegir un cuadrante aleatorio (índices de fila y columna)
    cuadrante_columna = random.randint(0, 1) * 2
    numeros = list(range(1, 5))  # Crear una lista de números del 1 al 4 y mezclarla aleatoriamente
    random.shuffle(numeros)
    for i in range(2):  # Llenar el cuadrante con los números aleatorios
        for j in range(2):
            matriz[cuadrante_fila + i][cuadrante_columna + j] = numeros.pop()
    return matriz

#==========Se encarga de llenar la matriz solucionada de ceros para poder rellenarla==========
def cerosRandom(matriz, numCeros): #Segun la cantidad de ceros(dificultad) busca pociciones i,j aleatoriamente y la llena con ceros para poner solucines
    if numCeros > len(matriz) * len(matriz[0]):
        raise ValueError("El número de ceros no puede ser mayor que el tamaño de la matriz.") #valida que la cantidad de ceros sea menor que la cantidad de entradas de la matriz
    matriz_copia = copy.deepcopy(matriz)
    fila, columna = len(matriz_copia), len(matriz_copia[0])
    posiciones = [(i, j) for i in range(fila) for j in range(columna)]
    random.shuffle(posiciones)
    for i in range(numCeros):
        fila, columna = posiciones[i]
        matriz_copia[fila][columna] = 0
    return matriz_copia #Retorna una copia de matriz para no alterar la matriz original y poder iterear en otras funciones

#==========se encarga de ir guardando los cambios que se la vna haciendo a la función==========
def guardarJugada(matrizConCeros,matriz, fila, columna, valor): #Toma un valor y lo evalua con la la matriz original y si hay un espacio vacio en la matriz con con ceros y los sutituye en las coordenadas correspondientes
    if matrizConCeros[fila-1][columna-1]==0:
        if matriz[fila-1][columna-1]==valor:
            print("\nEl valor es correcto\n")
            matrizConCeros[fila-1][columna-1] = valor
            return True
        else:
            print("\nEl valor es incorrecto\n")
            return False
    else:
        print("\nLa posicion fila = " + str(fila) + " columna = " + str(columna) + " ya posee un valor, intenta de nuevo\n")
        return False
    
#==========se ver si la matriz con ceros esta llena o aun tiene capos con 0========== 
def matrizLlena(matriz): #Determina si la matriz con ceros está llena de numeros diferentes de cero y retorna verdadero o falso para salir del ciclo en el programa principal
    for fila in range(len(matriz)):
        for columna in range(len(matriz)):
            if(matriz[fila][columna]== 0):                
                return False
    return True

