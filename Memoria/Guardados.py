import datetime as dt

def Comparar():
    recibir="si"
    try:
        with open("Guardados.txt","x") as archivo:
            crear(archivo, recibir)
    except FileExistsError:
        Cargar(archivo, recibir)

def crear(elemento,recibir):
    NewArch=elemento
    NewArch.write(recibir)

def Cargar(archivo, recibir):
    archivo.write(str(recibir)+"\n")

def CrearPaquete():
    ahora=dt.now
    formato=ahora.strftime("%d-%m %H:%M")
    tipo=0
    paquete=[]
    