#!/usr/bin/python3
"""
─────────────────────────────────────────────────────────────────────────────────────
PRÁCTICA 11: MENU CON TODAS LAS PRÁCTICAS
─────────────────────────────────────────────────────────────────────────────────────
Autor: Joel Francisco Escobar Socas
Asignatura: Seguridad en Sistemas Informáticos
Centro: Escuela Técnica Superior de Ingeniería Informática 
Contacto: alu0101130408@ull.edu.es
─────────────────────────────────────────────────────────────────────────────────────
Compilación --> python EncryptJoel.py
Nota: tener previamente instalado python en el ordenador
Link para la instalación: https://docs.microsoft.com/es-es/windows/python/beginners 
─────────────────────────────────────────────────────────────────────────────────────
"""
#─────────────────────────────────────────────────────────────────────────────────────
# MODULOS IMPORTADOS DE OTRAS PRÁCTICAS
#─────────────────────────────────────────────────────────────────────────────────────
import os
from src import vigenere_joelescobar #Practica 1
from src import rc4_joelescobar      #Practica 2
from src import chacha20_joel        #Practica 3
from src import CAGPS_JoelEscobar    #Practica 4
from src import aes_joelescobar      #Practica 6
from src import gamal_joel           #Practica 8
from src import rsa_joel             #Practica 9
from src import feigefiatshamir_joel #Practica 11

#─────────────────────────────────────────────────────────────────────────────────────
# FUNCIONES
#─────────────────────────────────────────────────────────────────────────────────────
def EncabezadoMenu():
    
    print("────────────────────────────────────")
    print("PRÁCTICA 11: MENU CON TODAS LAS PRÁCTICAS")
    print(" └> Por: Joel Francisco Escobar Socas")
    print("────────────────────────────────────")
    print("───────────/OPCIONES/───────────")
    print("Pulse 0. Para salir de la ejecución del programa")
    print("Pulse 1. Utilizar el Cifrado de Vigenere")
    print("Pulse 2. Utilizar el Algoritmo RC4")
    print("Pulse 3. Utilizar el Cifrado C/A de GPS")
    print("Pulse 4. Utilizar el AES")
    print("Pulse 6. Utilizar el Cifrado de Vigenere")
    print("Pulse 8. Utilizar El Gamal")
    print("Pulse 9. Utilizar el Algoritmo RSA")
    print("Pulse 11. Utilizar el Protocolo Feige-Fiat-Shamir")

#─────────────────────────────────────────────────────────────────────────────────────
# FUNCION PRINCIPAL QUE EJECUTA EL MENU
#─────────────────────────────────────────────────────────────────────────────────────
def main():
    while True:
        EncabezadoMenu()
        OpcionIntroducida = int(input("Seleccione una Opción >> "))
        if OpcionIntroducida == 1:
            vigenere_joelescobar.Practica1()
        elif OpcionIntroducida == 2: 
            rc4_joelescobar.Practica2()
        elif OpcionIntroducida == 3:
            chacha20_joel.Practica3()
        elif OpcionIntroducida == 4:
            CAGPS_JoelEscobar.Practica4()
        elif OpcionIntroducida == 5:
            print(" >>> Lo siento, esta práctica no ha sido implementada")
        elif OpcionIntroducida == 6:
            aes_joelescobar.Practica6()
        elif OpcionIntroducida == 7:
            print(">>> Lo siento, esta práctica no ha sido implementada")
        elif OpcionIntroducida == 8:
            gamal_joel.Practica8()
        elif OpcionIntroducida == 9:
            rsa_joel.Practica9()
        elif OpcionIntroducida == 10:
            print(">>> Lo siento, esta práctica no ha sido implementada")
        elif OpcionIntroducida == 11:
            feigefiatshamir_joel.Practica11()
        elif OpcionIntroducida == 0: 
            os.system('cls')
            print(">> Saliendo...")
            break
        else:
            print("¡ALERTA!")
            print(">> Seleccione una opción valida entre el 1 y el 3 <<")

#Llamada a la función principal
if __name__ == '__main__':
    main()