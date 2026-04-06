import datetime as dt

ident=0

def Comparar():
    recibir="si"
    llegada = "dados"
    
    try:
        with open("Guardados.txt","x") as archivo:
            crear(archivo, recibir)
    except FileExistsError:
        with open("Guardados.txt","a") as archivo:
            crear(archivo, recibir)

def crear(elemento,recibir):
    NewArch=elemento
    datazo=recibir
    llegada = "dados"
    NewArch.write(CrearPaquete(datazo, llegada)+"\n")

def Cargar(ele, recibir):
    llegada = "dados"
    Arch=ele
    dato=recibir
    Arch.write(CrearPaquete(dato, llegada)+"\n")

def CrearPaquete(Dato, llegada):
    ahora=dt.time
    formato=ahora.isoformat
    id=ident
    tipo=str(type(Dato))
    #paquete= [ID, fecha, tipo de dato, Valor, de donde salio]
    paquete=[id, formato, tipo, str(Dato), str(llegada)]
    id+=1
    return paquete
    
Comparar()