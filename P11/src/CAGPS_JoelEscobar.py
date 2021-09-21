#!/usr/bin/python3
"""
PRÁCTICA 4: GENERADOR C-A GPS
----------------------------------------------
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
----------------------------------------------
Compilación --> python cagps.py
nota: tener previamente instalado python en el ordenador
"""

import os
#Definición de la asignación de los códigos de los satelites tal como aparece ne la tabla
SV = {
   1: [2,6],
   2: [3,7],
   3: [4,8],
   4: [5,9],
   5: [1,9],
   6: [2,10],
   7: [1,8],
   8: [2,9],
   9: [3,10],
  10: [2,3],
  11: [3,4],
  12: [5,6],
  13: [6,7],
  14: [7,8],
  15: [8,9],
  16: [9,10],
  17: [1,4],
  18: [2,5],
  19: [3,6],
  20: [4,7],
  21: [5,8],
  22: [6,9],
  23: [1,3],
  24: [4,6],
  25: [5,7],
  26: [6,8],
  27: [7,9],
  28: [8,10],
  29: [1,6],
  30: [2,7],
  31: [3,8],
  32: [4,9],
}

#Función que hace el desplazamiento a la derecha y el calculo de la salida
def shift_right(register, feedback, salida):

    
    # calculo de la salida
    out = [register[i-1] for i in salida]
    if len(out) > 1: 
        out = sum(out) % 2
    else: 
        out = out[0]
        
    # Suma de modulo 2 de la retroalimentación
    realimentacion = sum([register[i-1] for i in feedback]) % 2
    # desplazamiento a la derecha 
    for i in reversed(range(len(register[1:]))):
        register[i+1] = register[i]

    register[0] = realimentacion
   
    return out
    
# Función que define el generador PRN
def PRN(sv,leng):

    # Inicialización de los registros, creamos los dos registros LFSR1 y LFSR2 y lo llenamos con "1" 
    LFSR1 = [1 for i in range(10)]
    LFSR2 = [1 for i in range(10)]
    #Creamos el vector que contendra el resultado lo denominamos C/A
    ca = [] 
    
    # Creamos la secuencia para toda la longitud especificada
    for i in range(leng):
        #desplazamos a la derecha 
        generator1 = shift_right(LFSR1, [3,10], [10])
        generator2 = shift_right(LFSR2, [2,3,6,8,9,10], SV[sv]) 

        #Sumamos en modulo dos y añadimos al codigo generado el resultado
        ca.append((generator1 + generator2) % 2)
    
    # Mostramos la secuencia generada
    print ("El resultado es:",ca)
    
#Función que muestra la cabecera del programa
def information():
    os.system("cls")
    print("PRACTICA 4: Generador C/A de GPS")
    print("Autor: Joel Francisco Escobar Socas")
    print("───────────────────────────────────────")
    

#Función principal del menu
def Practica4():

    information()
    #Recogemos por teclado el ID y la longitud
    IDsatelite = int(input(">> Introduzca el ID del Satélite: ")) 
    leng = int(input(">> Introduzca la longitud de la secuencia de salida: "))
    print("───────────────────────────────────────────────────────────────────")
    #Llamamos la funcion PRN que ejecuta el generador
    PRN(IDsatelite,leng)
