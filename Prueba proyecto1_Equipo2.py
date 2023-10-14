from Funciones_Pryecto1_equipo2 import *
import random
import copy

"Código de prueba"

N = 0
while N != 1 and N != 2:
    try:
        N = int(input('Digite "1" para resolver un Sudoku 4x4 o "2" para uno 9x9: '))
        if N != 1 and N != 2:
            print("Por favor, ingrese solo 1 o 2.")
    except ValueError:
        print("Por favor, ingrese solo 1 o 2 como un número entero.")
        
continuar4X4 = True
if N == 1:
    matriz=(resolver_sudoku((llenarCuadranteAleatorio4x4((crearMatriz4x4())))))
    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3:
        try:
            opcion = int(input("Por favor, ingrese 1 para el nivel fácil, 2 para el nivel intermedio o 3 para el nivel difícil: "))
            
            if opcion == 1:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,8)
                imprimirMatriz(matrizConCeros)
            elif opcion == 2:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,10)
                imprimirMatriz(matrizConCeros)
            elif opcion == 3:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,12)
                imprimirMatriz(matrizConCeros)
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Por favor, ingrese solo 1, 2 o 3 como un número entero.")
    
    while continuar4X4:
        # Solicitar el valor a jugar
        solicitarValor = True

        while solicitarValor:
            try:
                valor=validarEntradaEntera(input("Ingrese el valor deseado, este debe ser del 1 al 4: "))
                
                if validarNumeroEnRango(valor, 1, len(matrizConCeros)):
                    solicitarValor = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))
                    

        # Solicitar la fila a jugar
        solicitarFila = True

        while solicitarFila:
            try:
                fila=validarEntradaEntera(input("Ingrese la fila a modificar, este debe ser del 1 al 4: "))

                if validarNumeroEnRango(fila, 1, len(matrizConCeros)):
                    solicitarFila = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))

        # Solicitar la columna a jugar
        solicitarColumna = True

        while solicitarColumna:
            try:
                columna=validarEntradaEntera(input("Ingrese la columna a modificar, este debe ser del 1 al 4: "))

                if validarNumeroEnRango(columna, 1, len(matrizConCeros)):
                    solicitarColumna = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))
        
        #Ingresa la jugada a la matriz para verificar si es correcta o no
        # Si el valor es correcto lo almacena en matrizConCeros
        valorCorrecto = guardarJugada(matrizConCeros,matriz, fila, columna, valor)

        # Imprime la matriz actualizada
        imprimirMatriz(matrizConCeros)

        # Valida si la matriz ya se encuentra completada y si es asi finalizar el juego
        if matrizLlena(matrizConCeros):
            continuar4X4 = False            
            print("\nFelicidades has completado el sudoku!")
            
            
continuar9x9 = True
if N == 2:
    matriz=(resolver_sudoku((llenarCuadranteAleatorio9x9((crearMatriz9x9())))))
    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3:
        try:
            opcion = int(input("Por favor, ingrese 1 para el nivel fácil, 2 para el nivel intermedio o 3 para el nivel difícil: "))
            if opcion == 1:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,45)
                imprimirMatriz(matrizConCeros)
            elif opcion == 2:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,52)
                imprimirMatriz(matrizConCeros)
            elif opcion == 3:
                print ("La solucion es del sudoku:")
                imprimirMatriz(matriz)
                print ("El sudoku a resolver es:")
                matrizConCeros=cerosRandom(matriz,59)
                imprimirMatriz(matrizConCeros)
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Por favor, ingrese solo 1, 2 o 3 como un número entero.")
    
    while continuar9x9:
        # Solicitar el valor a jugar
        solicitarValor = True

        while solicitarValor:
            try:
                valor=validarEntradaEntera(input("Ingrese el valor deseado, este debe ser del 1 al 9: "))
                
                if validarNumeroEnRango(valor, 1, len(matrizConCeros)):
                    solicitarValor = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))
                    

        # Solicitar la fila a jugar
        solicitarFila = True

        while solicitarFila:
            try:
                fila=validarEntradaEntera(input("Ingrese la fila a modificar, este debe ser del 1 al 9: "))

                if validarNumeroEnRango(fila, 1, len(matrizConCeros)):
                    solicitarFila = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))

        # Solicitar la columna a jugar
        solicitarColumna = True

        while solicitarColumna:
            try:
                columna=validarEntradaEntera(input("Ingrese la columna a modificar, este debe ser del 1 al 9: "))

                if validarNumeroEnRango(columna, 1, len(matrizConCeros)):
                    solicitarColumna = False
                    
            except TypeError as error:
                print(str(error))
            except Exception as error:
                print(str(error))
        
        #Ingresa la jugada a la matriz para verificar si es correcta o no
        # Si el valor es correcto lo almacena en matrizConCeros
        valorCorrecto = guardarJugada(matrizConCeros, matriz, fila, columna, valor)

        # Imprime la matriz actualizada
        imprimirMatriz(matrizConCeros)

        # Valida si la matriz ya se encuentra completada y si es asi finalizar el juego
        if matrizLlena(matrizConCeros):
            continuar9x9  = False            
            print("\nFelicidades has completado el sudoku!")
