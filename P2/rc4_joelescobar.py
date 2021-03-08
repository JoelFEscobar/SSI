#!/usr/bin/python3
"""
PRÁCTICA 2: CIFRADO DE CR4
----------------------------------------------
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
----------------------------------------------
Compilación --> python rc4.py
"""

import os
#Método KSA para el cifrado RC4
def KSA(key):
    i = 0
    klenght = len(key)

    S = list(range(256)) #Vector S de 256 elementos
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % klenght]) % 256 #key[i % klenght] es el vector T
        S[i], S[j] = S[j], S[i] #Intercambio de posiciones
    return S

#Método PGRA para el cifrado RC4
def PGRA(S, tamaño_mensaje):
    i = 0
    j = 0
    key = []
    while tamaño_mensaje > 0:
        tamaño_mensaje = tamaño_mensaje - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] 
        K = S[(S[i] +  S[j]) % 256]
        key.append(K)
    return key

# Visualizacion de un minimenu para usar diferentes visualizaciones
def menu():
    os.system("cls")
    print("====/ Opciones Posibles/=====")
    print("> Pulse 1: Si desea cifrarlo en decimal")
    print("> Pulse 2: Si desea cifrarlo en Hexadecimal")

#Funcion que convierte a ascii un vector
def ascii(Message,Messagelenght):
    Mascii = []
    i = 0
    for i in range(Messagelenght):
        Mascii.append(ord(Message[i]))
    return Mascii

#Funcion que lleva a cabo la suma XOR para cifrar
def sumaXOR(Msequence,AsciiM,Messagelenght):
    resultado = []
    i = 0
    for i in range(Messagelenght):
        resultado.append(Msequence[i] ^ AsciiM[i])
    return resultado

#Función que convierte el resultado en Hexadecimal
def hexadec(cifrado):
    hexadecimal =[]
    for i in range(len(cifrado)):
        hexadecimal.append(hex(cifrado[i]))
    return hexadecimal

#Funcion Principal
def main():
    print("PRACTICA 2: CIFRADO RC4")
    print("Autor: Joel Francisco Escobar Socas\n")
    keyintroduced = str(input(">> Introduzca una clave: "))
    #Convierte en valores Ascii cada carácter de la clave que se introduce
    keyintroduced = [ord(c) for c in keyintroduced] 
    #Llamada a KSA
    S = KSA(keyintroduced)

    message = str(input(">> Introduzca el mensaje que desea cifrar: "))
    Mlenght = len(message)

    #Llamada a PGRA
    sequence = PGRA(S, Mlenght)
    
    #Pasar los caracteres del vector a ascii
    Mascii = []
    Mascii = ascii(message, Mlenght)
    
    #Aplicar la suma XOR a ambas cadenas para cifrar
    Mcifrado = [] 
    Mcifrado = sumaXOR(sequence, Mascii, Mlenght)  
 
    #Introducimos un menu para preguntar si desea visualizarlo en decimal o hexadecimal
    menu()
    DecOrHex=int(input(">> ¿Qué desea hacer?: "))
    if DecOrHex == 1: 
        os.system("cls")
        print(">> Mensaje cifrado en Decimal:\n",">>" ,Mcifrado)
    elif DecOrHex == 2:
        os.system("cls")
        print("Mensaje en Hexadecimal:\n", ">>", hexadec(Mcifrado))   
    else:
        print(" >> Introduzca una opción valida entre el 1 y el 3") 


    

   
 
    

    
       
   

main()