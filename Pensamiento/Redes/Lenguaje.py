import os

check= False

def Control():
   ruta = "Diccionario.txt"
   if os.path.exists(ruta):
       check = True
   else:
       CrearDiccionario()
       

def Inicial():
    Control()
    while check == True:
        return None
    return None

def CrearDiccionario():
    with open("Diccionario.txt", "a")as Dicc:
        Dicc.write(("hola")+",")
        check=True

def ampliar(Palabra):
    with open("Diccionario.txt", "a+") as Dicc:
        if Palabra not in Dicc:
            Dicc.write(Palabra+",")
            
def Cargar():
    with open("Diccionario.txt", "r") as Dicc:
        Carga= [Linea.strip().split(",") for Linea in Dicc]
        return Carga    
    
def ErrorExistente():
    return None

