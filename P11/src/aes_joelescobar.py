#!/usr/bin/python3

"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 6: CIFRADO AES (Rinjdael)
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python aes_joel.py
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
# ESTRUCTURAS DEFINIDAS
#─────────────────────────────────────────────────────────────────────────────────────
# Inicialización de la Caja S
SBox = []
SBox.append([0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76])
SBox.append([0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0])
SBox.append([0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15])
SBox.append([0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75])
SBox.append([0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84])
SBox.append([0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf])
SBox.append([0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8])
SBox.append([0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2])
SBox.append([0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73])
SBox.append([0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb])
SBox.append([0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79])
SBox.append([0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08])
SBox.append([0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a])
SBox.append([0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e])
SBox.append([0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf])
SBox.append([0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16])

# Declaración del polinomio fijo utilizado para la expansión de las claves
RCON = []
RCON.append([0x01, 0x00, 0x00, 0x00])
RCON.append([0x02, 0x00, 0x00, 0x00])
RCON.append([0x04, 0x00, 0x00, 0x00])
RCON.append([0x08, 0x00, 0x00, 0x00])
RCON.append([0x10, 0x00, 0x00, 0x00])
RCON.append([0x20, 0x00, 0x00, 0x00])
RCON.append([0x40, 0x00, 0x00, 0x00])
RCON.append([0x80, 0x00, 0x00, 0x00])
RCON.append([0x1b, 0x00, 0x00, 0x00])
RCON.append([0x36, 0x00, 0x00, 0x00])

#─────────────────────────────────────────────────────────────────────────────────────
# FUNCIONES DEL ALGORITMO AES (RIJNDAEL - 128 bits)
#─────────────────────────────────────────────────────────────────────────────────────
# Función ColumnSubBytes: 
# Encargadas de sustituir los bytes del vector basada en la Caja S.

def ColumnSubBytes(col):
	for i in range(4):
        # Comprobamos si el número hexadecimal tiene una sola cifra
		if len(hex(col[i])[2:]) == 1:  
			Punto1 = 0
			Punto2 = col[i]
		else:
			Punto1 = int(hex(col[i])[-2], 16) 
			Punto2 = int(hex(col[i])[-1], 16) 
		col[i] = SBox[Punto1][Punto2]

# Función SubBytes: 
# Se ejecuta una sustitución de cada uno de los 16 bytes de la matriz de estado mediante la Caja S.

def SubBytes(State):
	for i in range(4):
		for j in range(4):
			if len(hex(State[i][j])[2:]) == 1:  
				Punto1 = 0
				Punto2 = State[i][j]
			else:
				Punto1 = int(hex(State[i][j])[-2], 16)  
				Punto2 = int(hex(State[i][j])[-1], 16) 
			State[i][j] = SBox[Punto1][Punto2]

# Función ShiftRow: 
# Consiste en una permutación de las filas de la matriz de estado.
# La primera fila no rota, la segunda fila rota 1 byte, la tercera fila rota 2 bytes 
# y asi sucesivamente

def ShiftRows(State):
	for i in range(4):
		for j in range(i):
			pos1 = State[0].pop(i)
			pos2 = State[1].pop(i)
			pos3 = State[2].pop(i)
			pos4 = State[3].pop(i)

			State[0].insert(i, pos2)
			State[1].insert(i, pos3)
			State[2].insert(i, pos4)
			State[3].insert(i, pos1)

# Función MixCol:
# Encargadas de multiplicar cada una de las columnas de la matriz de estado por un polinomio fijo 
def MixCol(col):
	Vec1 = []
	Vec2 = []
	for i in range(4):
		Vec1.append(col[i])
		aux = col[i] & 0x80
		Vec2.append((col[i] << 1) % 256)
		if aux == 0x80:
			Vec2[i] = Vec2[i] ^ 0x1b

	col[0] = Vec2[0] ^ Vec1[3] ^ Vec1[2] ^ Vec2[1] ^ Vec1[1]
	col[1] = Vec2[1] ^ Vec1[0] ^ Vec1[3] ^ Vec2[2] ^ Vec1[2]
	col[2] = Vec2[2] ^ Vec1[1] ^ Vec1[0] ^ Vec2[3] ^ Vec1[3]
	col[3] = Vec2[3] ^ Vec1[2] ^ Vec1[1] ^ Vec2[0] ^ Vec1[0]

# Función AddRoundKey: 
# Realiza la suma XOR de cada vuelta ejecutada en el main con los valores de la matriz de estado.
def AddRoundKey(message, key):
	for i in range(4):
		MidCol = []
		for j in range(4):
			MidCol.append(message[i][j] ^ key[i][j])
		message[i] = MidCol

#─────────────────────────────────────────────────────────────────────────────────────
# PROGRAMA PRINCIPAL (MAIN)
#─────────────────────────────────────────────────────────────────────────────────────
# Función Main donde se llama de forma estructurada a las funciones del algoritmo
def Practica6():
    print("────────────────────────────────────")
    print("PRÁCTICA 6: CIFRADO AES (RIJNDAEL)")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")
    
    # Se pide el mensaje del usuario por teclado en Hexadecimal
    OriginalMessage = str(input(">> Introduzca un mensaje (En Hexadecimal): "))
    while len(OriginalMessage) != 32:
        OriginalMessage = str(input(">> Error! Introduzca un mensaje de 16 bytes en Hexadecimal: "))
    
    # Se divide el mensaje del usuario y se guarda en forma de matriz
    Message = [] 
    for i in range(4):
        Message.append([])
        for j in range(4):
            pos = (i * 8) + (2 * j)
            Message[i].append(int(OriginalMessage[pos:pos+2], 16))


    # Pedimos por teclado la Clave que se quiera añadir en Hexadecimal
    OriginalKey = str(input(">> Introduzca una clave (En Hexadecimal): "))
    while len(OriginalKey) != 32:
        OriginalKey = str(input(">> Error! Introduzca una clave de 16 bytes en Hexadecimal: "))
    
    # Se divide la clave introducida por el usuario y se guarda en forma de matriz
    ModifiedKey = []
    for i in range(4):
        ModifiedKey.append([])
        for j in range(4):
            pos = (i * 8) + (2 * j)
            ModifiedKey[i].append(int(OriginalKey[pos:pos+2], 16))


    #──────────────────────────────────────────────────────────
    # HACEMOS LA EXPANSIÓN DE LA CLAVE DURANTE 10 ITERACIONES
    #──────────────────────────────────────────────────────────
    # Vector donde se irán guardando las subclaves generadas
    subkey = []  
    subkey.append(ModifiedKey)  

    # Comenzamos la iteración 10 veces ya que  el algoritmo es de 128 bits
    for n in range(0, 10):
        AuxOriginalKey = []
        AuxCol = []
        Col1 = []
        Col2 = []
        Col3 = []
        Col4 = []
        
        for i in range(4):
            AuxCol.append(subkey[n][3][i])
        
        # RotWord:
        # Esta parte rota el primer byte de la ultima palabra de 4 bytes de la matriz 
        AuxVar = AuxCol.pop(0)
        AuxCol.append(AuxVar)
        
        # SubBytes
        # A esa palabra resultante le aplicamos la operación ColumnSubBytes
        ColumnSubBytes(AuxCol)
        
        # XOR
        # Sumamos con una XOR esta palabra con la palabra 3 posiciones mas atrás 
        # y con un vector RCON diferente para cada una de las 10 vueltas
        for i in range(4):
            Col1.append(subkey[n][0][i] ^ AuxCol[i] ^ RCON[n][i])
            Col2.append(subkey[n][1][i] ^ Col1[i])
            Col3.append(subkey[n][2][i] ^ Col2[i])
            Col4.append(subkey[n][3][i] ^ Col3[i])

        AuxOriginalKey.append(Col1)
        AuxOriginalKey.append(Col2)
        AuxOriginalKey.append(Col3)
        AuxOriginalKey.append(Col4)
        #Añadimos la subclave final generada a la lista de claves 
        subkey.append(AuxOriginalKey)  
    #───────────────────────────────────────────────────────────────────────────────────────────
    
    #Limpiamos la consola para imprimir el resultado
    os.system("cls")
    Middle = []
    # PRIMERA ITERACIÓN DEL ALGORITMO (SOLO ADDROUNDKEY)
    #──────────────────────────────────────────────────────
    AuxState = Message  
    AddRoundKey(AuxState, ModifiedKey)  
    Middle.append(AuxState)  

    # Mostramos la primera iteración por pantalla 

    print ("R0 (Subclave = ", end = '')
    for i in range(len(subkey[0])):
        for j in range(len(subkey[0][i])):
            print (hex(subkey[0][i][j])[2:].zfill(2), end = '')
    print (") = ", end = '')
    for i in range(len(Middle[0])):
        for j in range(len(Middle[0][i])):
            print(hex(Middle[0][i][j])[2:].zfill(2), end = '')
    print ()

    #HACEMOS LAS SIGUIENTES ITERACIONES DEL ALGORITMO EJECUTANDO EL SIGUIENTE ORDEN 
    # 1ro.SubBytes > 2do.ShiftRow > 3ro.MixCol > 4to.AddRoundKey
    
    for k in range(1, 10):
        AuxState = Middle[k-1]  
        SubBytes(AuxState)  
        ShiftRows(AuxState)  
        for i in range(4):
            MixCol(AuxState[i]) 
        AddRoundKey(AuxState, subkey[k])
        # Se guarda el estado Middle generado
        Middle.append(AuxState)  
        
        # Mostramos por pantalla estas iteraciones ejecutadas
        print ("R" + str(k) + " (Subclave = ", end = '')
        for i in range(4):
            for j in range(4):
                print (hex(subkey[k][i][j])[2:].zfill(2), end = '')
        print (") = ", end = '')
        for i in range(4):
            for j in range(4):
                print (hex(Middle[k][i][j])[2:].zfill(2), end = '')
        print ()

    #ULRIMA ITERACIÓN  DEL ALGORITMO EJECUTAMOS EL SIGUIENTE ORDEN 
    # 1ro.SubBytes > 2do.ShiftRows > 3ro.AddRoundKey
    #Estado auxiliar que se transformará hasta obtener el primer estado intermedio
    AuxState = Middle[-1]  
    SubBytes(AuxState)  
    ShiftRows(AuxState)  
    AddRoundKey(AuxState, subkey[-1])  
    Middle.append(AuxState)  

    # Mostramos por pantalla la última iteración
    print ("R10" + " (Subclave = ", end = '')
    for i in range(4):
        for j in range(4):
            print (hex(subkey[-1][i][j])[2:].zfill(2), end = '')
    print (") = ", end = '')
    for i in range(4):
        for j in range(4):
            print (hex(Middle[-1][i][j])[2:].zfill(2), end = '')
    print ()

    # Mostramos por pantalla el bloque de texto cifrado resultante al final de las operaciones
    print ()
    print (">> El Texto Cifrado es: ", end = '')
    for i in range(4):
            for j in range(4):
                print (hex(Middle[-1][i][j])[2:].zfill(2), end = '')


    print ()



'''
==================================================================================
Mensaje Original en Hexadecimal: 00112233445566778899aabbccddeeff 
Clave Original en Hexadecimal: 000102030405060708090a0b0c0d0e0f
Resultado Cifrado Esperado en Hexadecimal: 69c4e0d86a7b0430d8cdb78070b4c55a
==================================================================================
'''