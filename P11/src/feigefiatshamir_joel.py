#!/usr/bin/python3

"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 11: PROTOCOLO FEIGE-FIAT-SHAMIR
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python feigefiatshamir_joel.py
Nota: tener previamente instalado python en el ordenador
Link para la instalación: https://docs.microsoft.com/es-es/windows/python/beginners 
─────────────────────────────────────────────────────────────────────────────────────
"""
#───────────────────────────────────────────────────────────────────────────────────
# LIBRERIAS UTILIZADAS
#───────────────────────────────────────────────────────────────────────────────────
import os
import sys
import math
from random import shuffle, randrange
#───────────────────────────────────────────────────────────────────────────────────
# FUNCIONES
#───────────────────────────────────────────────────────────────────────────────────
def TestLehmanPeralta(primo):   
    #Genero una lista de enteros desde 1 hasta el numero primo-1
    ExponentePrimo = (primo-1)/2
    ListaEnteros = list(range(1,primo))
    #desordenamos la lista
    shuffle(ListaEnteros)
    #La truncamos
    if(len(ListaEnteros)>100):
        del ListaEnteros[100:]
    
    Uno = True
    NumPrime= True
    #Para todo i siempre que el numero primo sea primo
    i = 0
    while((i < len(ListaEnteros) and (bool(primo)))):
        #Aplicamos la exponenciación Modular
        ResultadoExp = ExponenciacionRapidaModular(ListaEnteros[i],ExponentePrimo,primo)
        if(ResultadoExp != 1): 
            Uno =  False                    #Si la exponenciacion es distinto de 1
            if(ResultadoExp != primo-1): 
                primo = False               #Entonces el primo es compuesto
        i = i+1

    if (bool(Uno)):             #Si existe i tal que el resultado de la exponenciacion es -1
        return False            #El numero primo es compuesto
    else:   
        return primo            #Sino tal vez el numero es primo

def ExponenciacionRapidaModular(Base, Exponente, Modulo):
    NumX = 1
    NumY = Base % Modulo
    aux = Exponente
    while(aux > 0):
        #Si el auxiliar es par
        if((aux % 2) == 0):
            NumY = (NumY * NumY) % Modulo
            aux = aux / 2
        #Si el auxiliar es impar
        else:
            NumX = (NumX * NumY) % Modulo
            aux = aux -1
    return NumX




def FFS(p,q, n,r, s1, S, a1):
    print("──────/RESULTADO:/──────")
    
    print("p: ", p)
    print("q: ", q)
    print("n: ", n)
    print("s1: ", s1)
    print("S: ", S)
    print("a1: ", a1)

    # r = randrange(n)
    print(">> El valor de R es: ", r)
    ComprobacionSigno(S)
    
    #Identificación pública de A:
    print("Indentificación pública de A: ")
    v1= (pow(s1, 2)) % n
    print(">> V1:", v1)
    #v2= pow(s2, 2) % n
    #print(">> V2:", v2)

    #Testigo: A envía a B
    X = (S * pow(r, 2))%n
    #Xfinal = X % n
    print(">> X: ", X)
    #Respuesta: A envía a B
    Y = (r * pow(s1, a1)) % n
    #Yfinal = Y % n
    print(">> Y: ", Y)

    #Verificación de B
    YComprobacion =  (pow(Y, 2)) % n 
    print(">> Y comprobada es:", YComprobacion)
    Xcomprobacion = (X * pow(v1, a1)) % n 
    print(">> X comprobada es:", Xcomprobacion)

#Función que comprueba que debe ser 0 o 1 
def EsCero(a1):
    if(a1 == 0):
        return True
    elif (a1 == 1):
        return True
    else:
        return False

#Funcion que comprueba el signo
def ComprobacionSigno(num):
    if num < 0:
        print(">> El numero", num, " Es negativo")
    elif num == 0:
        print(">> El numero", num, " Es Cero")
    elif num > 0:
        print(">> El numero", num, " Es Positivo")

#───────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL
#───────────────────────────────────────────────────────────────────────────────────
def Practica11():

    # Título de la práctica  
    print("────────────────────────────────────")
    print("PRÁCTICA 11: PROTOCOLO FEIGE-FIAT-SHAMIR")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")
    
    #Pedimos P
    p = int(input(">> Introduzca el numero primo p: "))

    while(not(bool(TestLehmanPeralta(p)))):
        print("!!ALERTA!!")
        print("->El número p introducido no es un primo positivo")
        p = int(input(">> Introduzca de nuevo el numero primo p en formato valido: "))

    #Pedimos Q
    q = int(input(">> Introduzca el numero primo q: "))

    while(not(bool(TestLehmanPeralta(q)))):
        print("!!ALERTA!!")
        print("->El número q introducido no es un primo positivo")
        q = int(input(">> Introduzca de nuevo el numero primo q en formato valido: "))

    #Calculamos el valor privado de N
    n = p*q
    print(">> El valor de N es: ", n)
    r = int(input(">> Introduzca el numero aleatorio r: "))

    #Introducimos la Identificación secreta de A
    s1 = int(input(">> Introduzca la identificacion secreta S1: "))
    while(s1 > n):
        print("ERROR! El numero introducido es mayor que n")
        s1 = int(input(">> Introduzca la identificacion secreta S1: "))
        
    #s2 = int(input(">> Introduzca la identificacion secreta S2: "))
    #while(s2 > n):
        #print("El numero introducido es mayor que N")
        #s2 = int(input(">> Introduzca la identificacion secreta S2: "))
        
    S = int(input(">> Introduzca el signo aleatorio S: "))
    #Introducimos el bit secreto a1
    a1 = int(input(">> Introduzca el primer bit A1: ")) 
    while(not(bool(EsCero(a1)))):
        print("ERROR! El numero introducido debe ser o '0' o '1'")
        a1 = int(input(">> Introduzca el primer bit A1: "))
    #Introducimos el bit secreto a2
    #a2 = int(input(">> Introduzca el segundo bit A2: "))
    #while(not(bool(EsCero(a2)))):
        #print("ERROR! El numero introducido debe ser o '0' o '1'")
        #a2 = int(input(">> Introduzca el primer bit A2: "))

    #Llamamos a la función que ejecuta el Protocolo
    FFS(p,q, n,r, s1, S, a1)




#Practica11()
'''
Entrada de la diapositiva:
────────────────────────────────────────────────────────────────────────
Ejemplo 1: 
entrada: 
p = 5
q = 13
r=11
S1 = 4
S = +1
A1= 1


resultados
N= 65
v1= 16
X =56
Y= 44
────────────────────────────────────────────────────────────────────────
'''