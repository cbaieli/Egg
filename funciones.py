def convertir_a_metros(millas, pies, pulgadas):
    return 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas

def principal():
    print ("Convierte medidas inglesas a sistema metrico")
    L = 10
    F = 23
    P = 45
    M = convertir_a_metros(L, F, P)
    print("La longitud es de ", M, " metros")


print(convertir_a_metros(10,10,10))