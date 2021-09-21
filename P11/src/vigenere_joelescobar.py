#!/usr/bin/python3
"""
PRÁCTICA 1: CIFRADO DE VIGENÈRE
----------------------------------------------
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
"""
import os
#Definición del Alfabeto
alfabeto="abcdefghijklmnopqrstuvwxyz"
# Función que Cifra
def cifrar(mensaje,clave):
    texto_cifrado=" "
    contador = 0
    for letra in mensaje:
        if alfabeto.find(letra) != -1:
            suma_total = alfabeto.find(letra) + alfabeto.find(clave[contador%len(clave)])
            modulo = int(suma_total) % len(alfabeto)
            #cifrado
            texto_cifrado = texto_cifrado + str(alfabeto[modulo]) 
            contador = contador + 1
    return texto_cifrado

# 
# Función que descifra
def descifrar(mensaje,clave):
    texto_descifrado=" "
    contador = 0
    for letra in mensaje:
        if alfabeto.find(letra) != -1:
            resta_total = alfabeto.find(letra) - alfabeto.find(clave[contador%len(clave)])
            modulo = int(resta_total) % len(alfabeto)
            #Descifrado
            texto_descifrado = texto_descifrado + str(alfabeto[modulo]) 
            contador = contador + 1
    return texto_descifrado


def menu():
    os.system('cls')
    print("PRACTICA 1: CIFRADO DE VINEGERE")
    print("====/Menu/====")
    print("Pulse 1. Cifrar un mensaje")
    print("Pulse 2. Descifrar un mensaje")
    print("Pulse 3. Para salir de la ejecución del programa")
  

# Visualizamos el resultado por pantalla
def Practica1():
    while True:
        menu()
        opcion_menu = int(input("Introduzca una opción >> "))
        if opcion_menu == 1:
            mensaje = str(input("mensaje que desea cifrar:")).lower()
            clave = str(input("palabra clave:")).lower()
            print("El mensaje una vez cifrado es:")
            print(cifrar(mensaje,clave))
            print ("")
            input("pulsa una tecla para continuar")
        elif opcion_menu == 2:
            mensaje = str(input("mensaje cifrado que desea descifrar:")).lower()
            clave = str(input("palabra clave:")).lower()
            print("El mensaje una vez descifrado es:")
            print(descifrar(mensaje,clave))
            print ("")
            input("pulsa una tecla para continuar")
		    
        elif opcion_menu == 3: 
            break
        else:
            print("introduzca una opción valida entre el 1 y el 3")

