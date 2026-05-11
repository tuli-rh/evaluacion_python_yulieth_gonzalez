"""Crear una función que reciba una lista de números enteros y genere una nueva lista solo con los números pares mayores a 10.
 Luego debe mostrar la nueva lista y la cantidad de elementos encontrados.
 """
 
def numParesMayor10(lista):
    numMayor10 = []

    for i in range(0, len(lista)):
        if lista[i] % 2 == 0 and lista[i] > 10:
            numMayor10.append(str(lista[i]))

    print(f"N° pares mayores a 10: {', '.join(numMayor10)}")

def ejercicioNumPares():
    limiteNum = int(input("Cuantos numeros quiere ingresar: "))
    lista = []
    for i in range(0, limiteNum):
        num = int(input("Ingresa un num entero: "))
        lista.append(num)
   
    numParesMayor10(lista)

ejercicioNumPares()
