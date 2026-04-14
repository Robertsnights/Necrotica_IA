import random
from Comprension import Menues
from Memoria import Guardados

Salida= "exit"
Eleccion=" "

def Inicio(base):
    Eleccion=base
    while Eleccion != Salida:
        Seleccion()
    if Eleccion==Salida:
        Menues.Inicio

def Seleccion():
    Tirada=input("que tipo de dado quieres tirar: ")
    P1= input("tiene bonificador: ")
    P2= input("tiene ventaja: ")
    P3= input("tiene desventaja: ")
    P4=input("cuantos dados: ")
    Lanzamiento(Tirada, P1, P2, P3, P4)


def Lanzamiento(valor1, res1, res2, res3, res4):
    bien=res2
    mal=res3
    boni=res1
    base=valor1
    cantidad=int(res4)
    if (bien =="si"):
        V1 = random.randint(1, int(base)) + int(boni)
        V2 = random.randint(1, int(base)) + int(boni)
        if (V1 > V2):
            Resultados(V1, base)
        else:
            Resultados(V2, base)
    elif(mal=="si"):
        V1 = random.randint(1, int(base)) + int(boni)
        V2 = random.randint(1, int(base)) + int(boni)
        if (V1 < V2):
            Resultados(V1, base)
        else:
            Resultados(V2, base)
    elif (bien =="no" and mal=="no"):
        if (base < "20"):
            for i in range(cantidad):
                V1 = random.randint(1, int(base)) + int(boni)
                i+=1
            Resultados(V1, base)
        else:
            V1 = random.randint(1, int(base)) + int(boni)
            Resultados(V1, base)

def Resultados(Valor, Vdado):
    Numero=Valor
    Resultado="El resultado del d "+ str(Vdado) +" es: "+ str(Numero)
    print(Resultado)
    Guardados.Comparar(Numero, "Dados")
    Inicial = input("¿quieres continuar?")
    Inicio(Inicial)
    