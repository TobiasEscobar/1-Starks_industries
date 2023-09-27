#Escobar Tobias Fabricio 
#1-J
#Clase 3

#Ejercicio Integrador Data Stark #01 (segunda entrega)

from os import system
system("cls")

from funciones_01 import *

def mostrar_menu():
    for opcion in menu:
        print(opcion)

menu = ["1.Mostrar nombres de los heroes:", "2.Mostrar peso e identidad del heroe de mayor fuerza: ",
        "3.Mostrar heroe con menor altura: ", "4.Mostrar promedio de pesos en heroes masculinos", 
        "5.Mostrar heroes mas fuertes que el promedio de heroes femeninos", "6.Salir: \n"]

seguir = True
while seguir:

    mostrar_menu()
    
    while True:
        respuesta = input("Ingresa una opcion: ")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if 1 <= respuesta <= 6:
                break
        print("Opción no válida. Ingresa un número del 1 al 6.")

    match respuesta:
        case 1:
            mostrar_nombres(lista_personajes)
        case 2:
            mostrar = mostrar_mayor_fuerza(lista_personajes)
            print(f"\n{mostrar}\n")
        case 3:
            mostrar = mostrar_menor_altura(lista_personajes)
            print(f"\n{mostrar}\n")
        case 4:
            mostrar = mostrar_promedio_masculinos(lista_personajes)
            print(f"\nEl peso promedio de los heroes masculinos es de: {mostrar}\n")
        case 5:
            mostrar = mostrar_fuertes_al_promedio(lista_personajes)
            print(f"\n{mostrar}\n")
        case 6:
            seguir = False