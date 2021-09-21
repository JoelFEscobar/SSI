#!/usr/bin/python3
"""
PRÁCTICA 3: CIFRADO DE ChaCha20
----------------------------------------------
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
----------------------------------------------
Compilación --> python chacha20_joel.py
nota: tener previamente instalado python en el ordenador
"""
#Libreria estandar
import os
#Funcion que hace el generador ChaCha20 
def chacha20(key,count,nonce) :
    #Definicion de la matriz 
    S = [0] * 16 
    #En los 4 primeros bits le pasamos el mensaje 
    S[:4] = (0x61707865,0x3320646e,0x79622d32,0x6b206574)  
    #En los 8 bits siguientes les pasamos la clave 
    S[4:12] = key
    #En el siguiente bit pasamos el contador
    S[12] = count
    #En los siguientes 3 bits restantes le pasamos el nonce
    S[13:16] = nonce

    #visualizacion
    print("\n>>Estado Inicial:\n")
    for c in range(16): 
        print( hex(S[c]), end=", ")
    print("\n")
    #creamos una segunda matriz que recoja los datos de la matriz inicializada    
    x = list(S)
    #y repetimos 20 veces aplicamos el quarter round
    for i in range(10):
        #columnas (odd round)
        QR(x,0,4,8,12)
        QR(x,1,5,9,13)
        QR(x,2,6,10,14)
        QR(x,3,7,11,15)
        #diagonales(even round)
        QR(x,0,5,10,15)
        QR(x,1,6,11,12)
        QR(x,2,7,8,13)
        QR(x,3,4,9,14)
    
    print("\n>> Estado tras las 20 iteraciones:\n")
    for c in range(16):
        print(hex(x[c]), end=", ")
    print("\n")
    #sumamos la posiciones del vector inicializado con el vector operado
    out = [0] * 16
    i = 0
    for i in range(16):
        out[i] = x[i] + S[i]
    print("\n>> Estado salida del generador:\n")
    #lo mostramos como hecadecimal
    for c in range(16):
        print (hex(out[c]), end=",")
    print("\n")
#Rota'x' bits de 32 bits 'n' bits a la izquierda 

#Funcion rotate que hace la operacion de rodar hacia la izquierda los bits
def ROTL(a,b):
    return ((a << b) & 0xffffffff) | a >> (32 - b)

#La operacion basica del algoritmo donde basicamente sumaremos ambos valores y luego y rotamos hacia la izquierda los bits con una suma XOR
def QR(x,a,b,c,d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = ROTL(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = ROTL(x[b] ^ x[c], 12)
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = ROTL(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = ROTL(x[b] ^ x[c], 7)


def Practica3():
    print("==========================================================")
    print("PRACTICA 3: GENERADOR CHACHA20")
    print("Autor: Joel Francisco Escobar Socas")
    
    key = (0x03020100, 0x07060504, 0x0b0a0908, 0x0f0e0d0c, 0x13121110 , 0x17161514 , 0x1b1a1918, 0x1f1e1d1c)
    count = (0x00000001)
    nonce = (0x09000000, 0x4a000000, 0x00000000)
    chacha20(key,count,nonce)



"""
Resultado esperado:

estado inicial:
    61707865 3320646e 79622d32 6b206574
    03020100 07060504 0b0a0908 0f0e0d0c
    13121110 17161514 1b1a1918 1f1e1d1c
    00000001 09000000 4a000000 00000000

Estado final tras 20 iteraciones:

    837778ab e238d763 a67ae21e 5950bb2f
    c4f2d0c7 fc62bb2f 8fa018fc 3f5ec7b7
    335271c2 f29489f3 eabda8fc 82e46ebd
    d19c12b4 b04e16de 9e83d0cb 4e3c50a2

Estado del generador:

    e4e7f110 15593bd1 1fdd0f50 c47120a3
    c7f4d1c7 0368c033 9aaa2204 4e6cd4c3
    466482d2 09aa9f07 05d7c214 a2028bd9
    d19c12b5 b94e16de e883d0cb 4e3c50a2
"""