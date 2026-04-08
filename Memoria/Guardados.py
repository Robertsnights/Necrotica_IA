from datetime import datetime as dt

def Comparar():
    recibir="si"
    llegada = "dados"
    ident=int(RecordarID())
    try:
        with open("Guardados.txt","a") as archivo:
            ident+=1
            crear(ident, archivo, recibir)
            GuardarID(ident)
            
            
            
            
    except FileExistsError:
        with open("Guardados.txt","a") as archivo:
            ident+=1
            Cargar(ident, archivo, recibir)
            GuardarID(ident)
            

def crear(identificador, elemento , recibir):
    NewArch=elemento
    datazo=recibir
    identi=identificador
    llegada = "dados"
    NewArch.write(  " ".join(CrearPaquete(identi, datazo, llegada))+"\n")

def Cargar(identificador, ele, recibir):
    llegada = "dados"
    Arch=ele
    dato=recibir
    identi=identificador
    Arch.write( " ".join(CrearPaquete(identi, dato, llegada))+ "\n")

def CrearPaquete(ident, Dato, llegada):
    ahora=dt.now()
    formato=ahora.isoformat()
    id=ident
    tipo=str(type(Dato))
    #paquete= [ID, fecha, tipo de dato, Valor, de donde salio]
    paquete=[str(id), str(formato), str(tipo), str(Dato), str(llegada)]
    return paquete
 
def RecordarID():
    r=0
    with open("Regleta.txt","r") as Regla:
        r=int(Regla.read())
            
    return r

def GuardarID(Regla):
    r=Regla
    with open("Regleta.txt", "w") as Norma:
        Norma.write(str(r))
    return None
 
Comparar()