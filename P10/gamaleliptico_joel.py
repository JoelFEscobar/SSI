"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 10: CIFRADO ElGamal Elíptico
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python gamaleliptico_joel.py
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
# ESTRUCTURAS
#─────────────────────────────────────────────────────────────────────────────────────
 #y2= x3+ ax+ b

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
'''
def CalculoLamda(p,x,y):
    
    if(p == q):
        lamda = (3*pow(x, 2) + a)/(2*y) % p
    else:
        lamda = ()%p

    return lamda

'''
def ElGamalEliptico(p,a,b,db,da,mensaje,x,y):

    print("El valor 'p' es: ", p)
    print("El valor 'a' es: ", a)
    print("El valor 'b' es: ", b)
    
    print("El valor 'db' es: ", db)
    print("El valor 'da' es: ", da)
    print("El 'mensaje' es: ", mensaje)

    i=0
    j=0
    punto = []
    longitudpuntos = int(input("Introduzca la cantidad de puntos pertenecientes a la curva eliptica que desea calcular: "))
    for i in range(longitudpuntos):
        for j in range(longitudpuntos):
            cord1 = pow(y, 2) % p 
            cord2 = (pow(x, 3) + a*x + b) %p
            punto.append(cord1,cord2)
    print(punto)
#─────────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL
#─────────────────────────────────────────────────────────────────────────────────────

def main():
     # Título de la práctica  
    print("────────────────────────────────────")
    print("PRÁCTICA 10: EL GAMAL ELÍPTICO")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")

    #Solicitamos los Datos por teclado      
    G=[]
    #Introducimos el numero primo
    p = int(input("Introduzca el numero primo 'p': "))
    #comprobamos que es un numero primo a tarves del test de primalidad
    while(not(bool(TestLehmanPeralta(p)))):
        print("!!ALERTA!!")
        p = int(input(">> El numero introducido no es primo. Por favor, introduzca un numero primo: "))
    #introducimos a
    a = int(input("Introduzca el numero 'a': "))
    #comprobamos a
    while(a >= p):
        print(">> ERROR! El numero introducido no es menor que le numero primo")
        a = int(input("Introduzca un numero 'a' menor que el numero primo: "))
    #introducimos b
    b = int(input("Introduzca el numero 'b': "))
    #comprobamos b
    while(b >= p):
        print(">> ERROR! El numero introducido no es menor que le numero primo")
        b = int(input("Introduzca un numero 'a' menor que el numero primo: "))
    #introducimos el punto base
    x =int(input("Introduzca X: "))
    y =int(input("Introduzca Y: "))
    G=[x,y]
    #Comprobamos que el punto introducido pertenezca a la curva eliptica
    while(not((pow(y, 2)%p) == (pow(x, 3) + a*x + b)%p)):
        print(">> Error en el punto de la coordenada")
        x =int(input("Introduzca un punto X, siendo un punto valido de la curva y^2= x^3+ax+b: "))
        y =int(input("Introduzca un punto Y, siendo un punto valido de la curva y^2= x^3+ax+b: "))
        G=[x,y]

    
    
    #Introducimos la clave privada de b
    db = int(input("Introduzca el numero 'db': "))
    #Comprobamos la clave privada de b


    #Introducimos la clave privada de a
    da = int(input("Introduzca el numero 'da': "))
    #Comprobamos la clave privada de a

    mensaje=int(input("Introduzca el mensaje: "))

    #lamda = CalculoLamda(p, x, y)
    #Llamamos a la función el Gamal Elpitico para aplicar el algoritmo
    ElGamalEliptico(p,a,b,x,y,db,da,mensaje)

    
#Llamada del Main
if __name__ == '__main__':
    main()


'''
Aqui se muestra un ejemplo de como debería visualizarse el algoritmo
────────────────────────────────────────────────────────────────────────
Ejemplo: 

• Entradas:
p= 13
a= 5
b= 3
G= (9,6)
dB=2
dA=4
Mensaje original=2
• Salidas:
Puntos de la curva: (0,4),(0,9),(1,3),(1,10),(4,3),(4,10),(5,6),(5,7),(7,2),(7,11),(8,3),(8,10),(9,6),(9,7),
(10,0), (12,6),(12,7),
Clave pública de B: punto dBG=(9,7)
Clave pública de A: punto dAG=(9,6)
Clave secreta compartida calculada por A: 4*(9,7)=
Clave secreta compartida calculada por B: 2*(9,6)=
M=4
h=3<13/4
Mensaje original codificado como punto Qm =(2*3+1,2)=(7,2)
Mensaje cifrado y clave pública enviados de A a B: {Qm+dA*(dBG), dAG} = {(0,9), (9,6)}
────────────────────────────────────────────────────────────────────────
'''