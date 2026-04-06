from Logica import Matematicas, Dices

def lectura():
    busqueda=input("elija que hacer (1= matematicas, 2=dados ,dentro de poco): ")   
    if busqueda =="1":
        send=input("ingrese lo que desea: ")
        return cuentas(send)
    if busqueda == "2":
        retorno = Dices.Seleccion()
        return retorno
    
    
def cuentas(recepcion):
    match recepcion:
        case "Suma":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Suma(a,b)
            return (Resultado)
        case "Resta":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Resta(a,b)
            return (Resultado)
        case "Multi":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Multi(a,b)
            return (Resultado)
        case "Div":
            a=int(input("ingrese un valor: "))
            b=int(input("ingrese un valor: "))
            Resultado=Matematicas.Div(a,b)
            return (Resultado)
        case "Sumas":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Sumas(envio)
            return (Resultado)
        case "Restas":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Restas(envio)
            return (Resultado)
        case "Multis":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Multis(envio)
            return (Resultado)
        case "Divs":
            lista=input("ingrese un listado de numeros separados por un espacio: ")
            envio=lista.split()
            Resultado=Matematicas.Divs(envio)
            return (Resultado)