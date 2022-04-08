def formar_rectangulo(altura: int, anchura: int, Caracter: str) -> str:
    """Toma una altura, un ancho y un caracter y forma un rectangulo con esos datos"""

    for y in range(altura):
        for x in range(anchura):
            print(Caracter, end="")
        print("")


def formar_triangulo(anchura: int, caracter: str) -> str:
    """Toma una altura, un ancho y un caracter y forma un triangulo con esos datos"""

    contador: int = 1
    for i in range(anchura):
        espacios: int = anchura - contador
        print((" ") * espacios + (caracter + " ") * contador)
        contador += 1

def formar_triangulo_invertido(anchura: int, caracter: str) -> str:
    """Toma una altura, un ancho y un caracter y forma un triangulo con esos datos"""

    contador: int = anchura
    for i in range(anchura):
        espacios: int = anchura - contador
        print((" ") * espacios + (caracter + " ") * contador)
        contador -= 1


eleccion = int(input("ingrese que forma quiere formar: 1, cuadrado o 2, triangulo normal 0 3, triangulo invertido"))

if eleccion == 1:
        Alto = int(input("ingrese el alto del rectangulo que quiere formar: "))
        Ancho = int(input("ingrese el ancho del rectangulo que quiere formar: "))
        Caracter = input("ingrese el caracter que quiere usar para formar el rectangulo: ")
        formar_rectangulo(Alto, Ancho, Caracter)
elif eleccion == 2:
        Ancho = int(input("ingrese el ancho de la base del triangulo que quiere formar: "))
        Caracter = input("ingrese el caracter que quiere usar para formar el triangulo: ")

        formar_triangulo(Ancho, Caracter)
elif eleccion == 3:
        Ancho = int(input("ingrese el ancho de la base del triangulo que quiere formar: "))
        Caracter = input("ingrese el caracter que quiere usar para formar el triangulo: ")

        formar_triangulo_invertido(Ancho, Caracter)
