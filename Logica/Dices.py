import random
def Seleccion():
    Tirada=input("que tipo de dado quieres tirar: ")
    P1= input("tiene bonificador: ")
    P2= input("tiene ventaja: ")
    P3= input("tiene desventaja: ")
    P4=input("cuantos dados: ")
    lanzar= Lanzamiento(Tirada, P1, P2, P3, P4)
    return(lanzar)

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
            return V1
        else:
            return V2
    elif(mal=="si"):
        V1 = random.randint(1, int(base)) + int(boni)
        V2 = random.randint(1, int(base)) + int(boni)
        if (V1 < V2):
            return V1
        else:
            return V2
    elif (bien =="no" and mal=="no"):
        if (base < "20"):
            for i in range(cantidad):
                V1 = random.randint(1, int(base)) + int(boni)
                i+=1
            return V1
        else:
            V1 = random.randint(1, int(base)) + int(boni)
            return V1
