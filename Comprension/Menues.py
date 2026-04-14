from os import system as S
from Comprension import Ingresos
from Logica import Dices

L=""
respuesta=" "
salida="return"

def Inicio():
    bucle()

def bucle():
    while respuesta!=salida:
        S("cls")
        print("Escriba una de las opciones")
        L = input("Ayuda, 1,2,3")
        opciones(L)

def opciones(Recurso):
    match Recurso:
        case "Ayuda":
            Listado=["1 = Matematicas\n", "2 = Dados\n", "3 = \n"]
            for i in range(len(Listado)):
                print(Listado[i])
        case "1":
            Ingresos.lectura()
        case "2":
            Dices.Seleccion()
            