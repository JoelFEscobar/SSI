#!/usr/bin/python3

"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 8: CIFRADO ElGamal
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python gamal_joel.py
Nota: tener previamente instalado python en el ordenador
Link para la instalación: https://docs.microsoft.com/es-es/windows/python/beginners 
─────────────────────────────────────────────────────────────────────────────────────
"""
#─────────────────────────────────────────────────────────────────────────────────────
# LIBRERÍAS UTILIZADAS
#─────────────────────────────────────────────────────────────────────────────────────
import os
import sys
import math

#─────────────────────────────────────────────────────────────────────────────────────
# FUNCIONES
#─────────────────────────────────────────────────────────────────────────────────────

#Funcion que aplica el algoritmo de ElGamal
def ElGamal (p, a, k, x, m):
    # p - numero primo introducido
    # a - numero alpha
    # k - clave publica de A
    # x - clave secreta de B
    # m - mensaje introducido 

    print("\n")
    #Primero se generan las claves publicas y compartidas del usuario A y el usuario B
    Ya = pow(a, k) % p
    print(">> La clave publica de A generada es : ya = ", Ya)
    Yb = pow(a, x) % p
    print(">> La clave publica de B generada es: yb = ", Yb)
    
    BaseKA = pow(a,x)
    K = pow(BaseKA,k) % p
    print(">>La clave compartida generada en A es: K = ", K)

    #En estas lineas se genera la clave compartida de B que en este caso no es necesario porque es la misma que la de A
    #BaseKB = pow(a,k)
    #Kb = pow(BaseKB,x) % p
    #print(">>La clave compartida generada en N es: ", Kb)
    
    #Parte donde se cifra el mensaje  
    cifrado = K * m % p
    print(">> El mensaje cifrado C es : C = ", cifrado)

    #Parte donde se descifra el mensaje calculando la inversa
    inversaK = Inverso(K, p)
    print(">> Inversa de K: k-1 =", inversaK)
    descifrado = inversaK * cifrado % p
    print(">> El mensaje descifrado es:  M = ", descifrado)


# Funcion que aplica el Máximo comun divisor de euclides
# Baicamente devuelve un vector (d,x,y). Donde d será el mcd de los dos numeros y x es el inverso de a modulo b
def MCDEuclides(a,b):

    if b == 0:
        return a,1,0
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1

    while b != 0:
        q = a//b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        #Se actualizan los valores
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if a < 0:
        return map(int, (-a, -x2, -y2))
    return map(int, (a, x2, y2))

# Esta función calcula el inverso del modulo calculado
def Inverso(n1,n2):
    d,x,y = MCDEuclides(n1,n2)

    if d > 1:
        return ' CUIDADO! -> El inverso de este numero no existe!'
    else:
        return x % n2
 
#─────────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL
#─────────────────────────────────────────────────────────────────────────────────────
def main():
    
    # Título de la práctica  
    print("────────────────────────────────────")
    print("PRÁCTICA 8: CIFRADO ELGAMAL")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")

    # Se solicitan los números:
    p = int(input(">> Introduzca el numero P: ")) #sera publico
    a = int(input(">> Introduzca el numero A: ")) #sera publico 
    k = int(input(">> Introduzca el numero K: ")) 
    x = int(input(">> Introduzca el numero X: "))
    m = int(input(">> Introduzca el mensaje M: "))

    #Llamamos a la función encargada de ejecutar el algoritmo
    ElGamal(p, a, k, x, m)

#Llamada del Main
if __name__ == '__main__':
    main()


'''
Aqui se muestra un ejemplo de como debería visualizarse el algoritmo
────────────────────────────────────────────────────────────────────────
Ejemplo 1: 
entrada: p=13 a=4 k=5 x=2 m=8
salida:  ya=10 yb=3 K=9 C=7 K-1=3  M=8
────────────────────────────────────────────────────────────────────────
'''

