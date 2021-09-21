#!/usr/bin/python3

"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 7: CIFRADO AES - CBC (Cypher Block Chainning)
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python aescbc_joel.py
Nota: tener previamente instalado python en el ordenador
Link para la instalación: https://docs.microsoft.com/es-es/windows/python/beginners 
─────────────────────────────────────────────────────────────────────────────────────
"""

#─────────────────────────────────────────────────────────────────────────────────────
# LIBRERÍAS UTILIZADAS
#─────────────────────────────────────────────────────────────────────────────────────
import os
import sys

#─────────────────────────────────────────────────────────────────────────────────────
# FUNCIONES
#─────────────────────────────────────────────────────────────────────────────────────
def sumaXOR (vector1, vector2):
    salida = []
    if(vector1 != 32):
        print("El texto es menor")

    return  salida

def ciphertable(value):
    if(value == '00'):
        value = '01'
    elif(value == '01'):
        value = '10'
    elif(value == '10'):
        value = '11'
    elif(value == '11'):
        value = '00'


#─────────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL
#─────────────────────────────────────────────────────────────────────────────────────
def main():
    print("────────────────────────────────────")
    print("PRÁCTICA 7: CIFRADO AES MODO CBC")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")

    encrypt = []
    #Se solicita la clave en hexadecimal
    key = str(input(">> Introduzca una clave: "))
    while len(key) != 32:
        key = str(input(">> Error! Introduzca una clave de 16 bytes de lognitud en Hexadecimal: "))
    
    #Se solicita el vector de inicialización
    IVector = str(input(">> Introduzca el vector de Inicializacion: "))
    while len(IVector) != 32:
        IVector = str(input(">> Error! Introduzca un vector de inicialización de 16 bytes en Hexadecimal: "))
    
    #se solicitan los bloques 
    Block1=str(input(">> Introduzca el primer bloque de texto original: "))
    while len(Block1) != 32:
        Block1 = str(input(">> Error! Introduzca el primer bloque de texto de 16 bytes en Hexadecimal: "))
    
    Block2= str(input(">> Introduzca el segundo bloque de texto original: "))
    while len(Block2) != 32:
        Block2 = str(input(">> Error! Introduzca el segundo bloque de texto de 16 bytes en Hexadecimal: "))

    # Se hace una XOR con el vector de incializacion y el bloque de texto 1 
    # almaceno la salida en encrypt
    # el encrypt lo sumo con la clave 
    # la salida la almaceno en bloque de texto 2
    # 
    #se hace una XOR con el bloque de texto1 y con el bloque de texto 2
    # almaceno la salida en encrypt
    # el encrypt lo sumo con la clave 
    # la salida la almaceno en bloque de texto 2
    
