Mensaje=[]
Recuerdo=""
Validacion=" "

def lectura():
    with open("Guardados.txt", "r") as archivo:
        print("existe el archivo")
        Leido = [linea.strip().split(" ") for linea in archivo]
        return Leido
    return Leido
    
def recordar(Texto):
    if(Validacion== "si"):
        Mensaje.insert(0, Texto)
        while len(Mensaje)>15:
            del Mensaje[-1]


def contar():
    #posible ingreso de mas valores
    Cuentas=lectura()
    for i in Cuentas:
        match Cuentas[i][5]:
            case "dados":
                return None
    return None

def CrearSugerencia(Valores, Listas):
    control =0
    guardado=0
    Categorias=Listas
    Cantidad = len(Valores)
    for i in range(len(Valores)):
        Sumatoria+=Valores[i]
    Sumatoria= Sumatoria - Valores[0]
    media=Sumatoria/Cantidad
    Maximo= max(Valores)
    while control == 0:
        for i in range(len(Valores)):
            if Valores[i] >= Maximo:
                control+=1
                guardado=i
    
    if Maximo > media:
        imprimir=("quieres volver a: "+ str(Categorias[guardado]))
    
    return imprimir