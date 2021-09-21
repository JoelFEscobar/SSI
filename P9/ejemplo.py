  
###################################################################
## Universidad de La Laguna                                      ##
## Escuela Superior de Ingeniería y Tecnología                   ##
## Grado en Ingeniería Informática                               ##
## Seguridad en Sistemas Informáticos                            ##
## Fecha: 09/05/2017                                             ##
## Autor: Kevin Estévez Expósito (alu0100821390)                 ##
##                                                               ##
## Práctica 8: Cifrado RSA                                       ##
## Descripción: Implementación del cifrado de clave pública RSA. ##
##                                                               ##
## Ejecución: py rsa.py                                          ##
###################################################################


import sys
from random import shuffle


##### FUNCIONES #####

# Función de exponenciación rápida modular
def exp_rapida(base, exponente, modulo):
	x = 1
	y = base % modulo
	b = exponente
	while (b > 0):
		if ((b % 2) == 0):  # Si b es par...
			y = (y * y) % modulo
			b = b / 2
		else:  # Si b es impar...
			x = (x * y) % modulo
			b = b - 1
	return x

# Función de test de primalidad de Lehman Peralta
def lehman_peralta(p):
	a = list(range(1, p))  # Lista de enteros de 1 a 'p-1'
	shuffle(a)  # Se "baraja" la lista y se desordena
	# Si la lista tiene más de 100 elementos, se trunca la lista dejando solo los 100 primeros elementos
	if (len(a) > 100):
		del a[100:]
	todo_uno = True
	primo = True
	i = 0
    
	while ((i < len(a)) and (bool(primo))):
		aux = exp_rapida(a[i], (p-1)/2, p) 
		if (aux != 1):
			todo_uno = False
			if (aux != p-1):
				primo = False
		i = i + 1

	if (bool(todo_uno)):
		return False
	else:
		return primo

# Función de algoritmo de Euclides Extendido
def euclides_ext(a, b):
	x = [a, b]
	z = [1, 0]
	i = 1
	while (x[i] != 0):
		x = x + [x[i-1] % x[i]]
		z = z + [-(x[i-1] // x[i]) * z[i] + z[i-1]]
		i = i + 1
	return x[i-1], z[i-1]

	
##### PROGRAMA PRINCIPAL #####

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base = len(abecedario)

print ()
# Se pide el texto del mensaje a cifrar
mnsj_original = str(input("Introduzca el texto del mensaje a cifrar: "))
# Se eliminan los espacios del mensaje original y se pasa todo a mayúsculas
mnsj_original = mnsj_original.replace(' ', '').upper()

print ()
# Se pide el número primo 'p'
p = int(input("Introduzca el número primo 'p': "))
# Si no se ha introducido un 'p' primo positivo, se vuelve a pedir
while (not(bool(lehman_peralta(p)))):
	print ("El número 'p' debe ser un número primo positivo!")
	print ()
	p = int(input("Introduzca el número primo 'p': "))

# Se pide el número primo 'q'
q = int(input("Introduzca el número primo 'q': "))
# Si no se ha introducido un 'q' primo positivo, se vuelve a pedir
while (not(bool(lehman_peralta(q)))):
	print ("El número 'q' debe ser un número primo positivo!")
	print ()
	q = int(input("Introduzca el número primo 'q': "))

print ()
# Se calcula 'n' (p * q)
n = p * q
# Se muestra el 'n' obtenido
print ("n =", n)

# Se calcula 'phi' ((p-1)(q-1))
phi = (p - 1) * (q - 1)
# Se muestra el 'phi' obtenido
print ("phi =", phi)

print ()
# Se pide el número 'd' primo con 'phi'
d = int(input("Introduzca el número 'd' primo con phi: "))
aux, e = euclides_ext(d, phi)
if (e < 0):
	e = e + phi
# Si no se ha introducido un 'd' primo con 'phi', se vuelve a pedir
while (aux != 1):
	print ("El número 'd' debe ser un entero primo con phi")
	print ()
	d = int(input("Introduzca el número 'd' primo con phi: "))
	aux, e = euclides_ext(d, phi)
	if (e < 0):
		e = e + phi

print ()
# Se muestra el 'e' obtenido
print ("e =", e)

# Se calcula el tamaño de bloque en el que se dividirá el mensaje original
j = 2
while ((base ** j) < n):
	j = j + 1

mnsj_bloques = []  # Lista que contendrá los bloques del mensaje
i = 0
# Se divide el mensaje en bloques de longitud j-1
while (i < len(mnsj_original)):
	mnsj_bloques = mnsj_bloques + [mnsj_original[i:i+j-1]]
	i = i + j - 1

mnsj_bloques_decimal = []  # Lista que contendrá los bloques del mensaje convertidos en decimal

for i in mnsj_bloques:
	aux = 0  # Suma de los caracteres en decimal ponderados
	pos = j - 2  # Posición del caracter en el bloque para la ponderación
	k = 0
	while (k < len(i)):
		aux = aux + abecedario.find(i[k]) * (base ** pos)  # Se suma la ponderación del caracter correspondiente
		k = k + 1
		pos = pos - 1
	mnsj_bloques_decimal = mnsj_bloques_decimal + [aux]  # Se añade a la lista el bloque en decimal generado

print ()
# Se muestra los bloques del mensaje convertidos en decimal
print ("Texto en bloques de", j-1, "caracteres, pasado a decimal:", mnsj_bloques_decimal)


# ----- CIFRADO ----- #
print ()
print ("Cifrando...")

cifrado_bloques_decimal = []  # Lista que contendrá los bloques del mensaje cifrado en decimal
for i in mnsj_bloques_decimal:
	cifrado_bloques_decimal = cifrado_bloques_decimal + [exp_rapida(i, e, n)]  # Se cifra el bloque correspondiente

print ()
# Se muestra los bloques del mensaje cifrado en decimal
print ("Bloques cifrados:", cifrado_bloques_decimal)


# ----- DESCIFRADO ----- #
print ()
print ("Descifrando...")

descifrado_bloques_decimal = []  # Lista que contendrá los bloques del mensaje descifrado en decimal
pos = 0
for i in cifrado_bloques_decimal:
	descifrado_bloques_decimal = descifrado_bloques_decimal + [exp_rapida(i, d, n)]  # Se descifra el bloque correspondiendte

print()
# Se muestra los bloques del mensaje descifrados en decimal
print ("Bloques descifrados:", descifrado_bloques_decimal)


sys.exit(0)


