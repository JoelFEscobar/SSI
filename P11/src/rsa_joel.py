#!/usr/bin/python3

"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 9: CIFRADO RSA
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python rsa_joel.py
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
from random import shuffle
#─────────────────────────────────────────────────────────────────────────────────────
# DEFINICIONES
#─────────────────────────────────────────────────────────────────────────────────────
abecedario='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ABCLongitud=len(abecedario)
#─────────────────────────────────────────────────────────────────────────────────────
# FUNCIONES
#─────────────────────────────────────────────────────────────────────────────────────

#Funcion que calcula el test de primalidad de Lehman y Peralta
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

#Función que define el algoritmo extendido de Euclides
def AlgoritmoExtendidoEuclides(a,b):
    x = [a,b]
    z = [1,0]
    i = 1
    while(x[i] != 0):
        x = x + [x[i-1]%x[i]]
        z = z + [-(x[i-1]//x[i]) * z[i] + z[i-1]]
        i = i + 1
    return x[i-1], z[i-1]

#Calculo del Numero N que será el modulo de cifra de los primos
def CalculoN(p,q):
    NumN = p * q
    return NumN

#Calculo del numero Euler Phi
def CalculoEulerPhi(p,q):
    NumEulerPhi = (p-1) * (q-1)
    return NumEulerPhi

#Funcion que llama al algoritmo
def RSA(Mensaje, p, q, d, e):
    #calculo de n
    n = CalculoN(p, q)
    print(">> El numero n es: ", n)

    #Calculo de los Bloques
    ResultadoBloques = []
    ResultadoBloques = CalculoBloques(Mensaje,n)
    print (">>  El bloque en Decimal tras la división es: ", ResultadoBloques)

    #llamada a encrypt
    Cifrado = []
    Cifrado = encrypt(ResultadoBloques,e,n)
    print(">> Texto cifrado en Decimal: ", Cifrado)

def CalculoBloques(Message,n):

    #Calculo del tamaño en el que se divide el mensaje
    
    j = 2 
    while((ABCLongitud ** j) < n):
        j = j+1

    #Division del mensaje en bloques de j-1 de tamaño
    BloquesDelMensaje = []
    i = 0
    while(i < len(Message)):
        BloquesDelMensaje = BloquesDelMensaje + [Message[i:i + j - 1]]
        i = i + j - 1

    #Convertimos los bloques a decimal
    BloquesEnDecimal = []
    for i in BloquesDelMensaje:
        Suma = 0
        Posicion = j-2
        k = 0
        while(k < len(i)):
            #Se suma la ponderación del caracter correspondiente
            Suma = Suma+ abecedario.find(i[k]) * (ABCLongitud ** Posicion) 
            k = k + 1
            Posicion = Posicion - 1 
        # Se añade a la lista el bloque en decimal generado
        BloquesEnDecimal = BloquesEnDecimal + [Suma] 

    return BloquesEnDecimal
#Funcion encargada de cifrar
def encrypt(BloquesDecimal,e,n):
    
    BloquesCifrados = []
    for i in BloquesDecimal:
        BloquesCifrados = BloquesCifrados + [ExponenciacionRapidaModular(i, e, n)]

    return BloquesCifrados
#───────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL
#─────────────────────────────────────────────────────────────────────────────────────

def Practica9():
    # Título de la práctica  
    print("────────────────────────────────────")
    print("PRÁCTICA 9: CIFRADO RSA")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")

    #Solicitamos los Datos por teclado
    #El mensaje introducido
    MensajeIntroducido=str(input(">> Introduzca el Mensaje a cifrar: "))
    #Eliminamos los espacios del mensaje original 
    #Lo ponemos como mayuscula
    MensajeIntroducido= MensajeIntroducido.replace(' ', '').upper()

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


    #Calculo de EulerPhi
    EulerPhi = CalculoEulerPhi(p, q)
    print(">> El Euler Phi es: ", EulerPhi)

  
    
    #Pedimos D
    d = int(input(">> Introduzca el numero d: "))
    # Si no se ha introducido un 'd' primo con 'phi', se vuelve a pedir
    aux, e = AlgoritmoExtendidoEuclides(d, EulerPhi)
    if (e < 0):
	    e = e + EulerPhi
    # Si no se ha introducido un 'd' primo con 'phi', se vuelve a pedir
    while (aux != 1):   
	    print ("El número 'd' debe ser un entero primo con phi")
	    print ()
	    d = int(input("Introduzca el número 'd' primo con phi: "))
	    aux, e = AlgoritmoExtendidoEuclides(d, EulerPhi)
	    if (e < 0):
		    e = e + EulerPhi

    print(">> El numero e obtenido: ", e)
    # Llama a la función RSA para ejecutar el algoritmo
    RSA(MensajeIntroducido, p, q, d ,e)



'''
Aqui se muestra un ejemplo de como debería visualizarse el algoritmo
────────────────────────────────────────────────────────────────────────
Ejemplo 1: 
entrada: Texto=MANDA DINEROS, p=421, q=7 y d=1619
salida:  son primos p y q
         si d es primo con o(n) = 2520
         e= 179
         n= 2947 division en 2 caracteres
         bloques = 312,341,3,221,121,382
         texto cifrado = 2074,2173,0404,2340,1789,2333
────────────────────────────────────────────────────────────────────────
'''

