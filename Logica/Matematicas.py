# Region Simples
def Suma(valor1, valor2):
    int(valor1)
    int(valor2)
    return valor1 + valor2

def Resta(valor1, valor2):
    int(valor1)
    int(valor2)
    return valor1-valor2

def Multi(valor1, valor2):
    int(valor1)
    int(valor2)
    return valor1*valor2

def Div(valor1, valor2):
    int(valor1)
    int(valor2)
    return valor1/valor2
# EndRegion

# Region Multiples
def Sumas(valores):
    resultado =0
    for i in range(len(valores)):
        k=int(valores[i])
        resultado += k    
    return resultado

def Restas(valores):
    resultado =0
    for i in range(len(valores)):
        k=int(valores[i])
        resultado -= k    
    return resultado

def Multis(valores):
    resultado =0
    for i in range(len(valores)):
        k=int(valores[i])
        resultado *= k    
    return resultado

def Divs(valores):
    resultado =0
    for i in range(len(valores)):
        k=int(valores[i])
        resultado /= k    
    return resultado
# EndRegion
