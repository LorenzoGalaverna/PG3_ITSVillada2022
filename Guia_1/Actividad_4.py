lista_ingreso = input("Escribe una lista de numeros separados por espacios: ")
lista = lista_ingreso.split()

def ordenar_lista_usuario(lista_sin_ordenar):
    for i in range(len(lista_sin_ordenar)):
        lista_sin_ordenar[i] = int(lista_sin_ordenar[i])
    lista_sin_ordenar.sort(reverse = True)
    print("su lista ordenada qudaria asi: ", lista_sin_ordenar)

ordenar_lista_usuario(lista)