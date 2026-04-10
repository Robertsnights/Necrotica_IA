from os import system as S
from Comprension import Ingresos

L=""
respuesta=" "
salida="return"

def bucle():
    while respuesta!=salida:
        S("cls")
        print("Escriba una de las opciones")
        L = input("Ayuda, 1,2,3,4")
        opciones(L)

def opciones(Recurso):
    match Recurso:
        case "Ayuda":
            Listado=["1 = Matematicas\n", "2 = Dados\n", "3 = Charla\n", "4= diagramar\n"]
            for i in range(len(Listado)):
                print(Listado[i])
        case "1":
            Ingresos.lectura()
            