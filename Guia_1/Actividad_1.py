lista_de_numeros = [1, 4, 2, 6, 7, 3]
print(lista_de_numeros)
numero_elejido_por_usuario = input("Escribe el numero que desea buscar: ")


def posicion_del_numero_en_la_lista(lista: list, numero: int) -> int:
    """Toma una lista y un numero y devuelve la posicion del numero en la lista"""

    posicion = lista.index(int(numero))
    print("El numero que buscas esta en la posicion: ", posicion)


posicion_del_numero_en_la_lista(lista_de_numeros, numero_elejido_por_usuario)