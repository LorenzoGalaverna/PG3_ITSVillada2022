numero = int(input("Escribe un numero para averiguar si es step: "))


def numero_step(num: int) -> int:
    """Toma una palabra y devuelve la cantidad de vocales que tiene"""

    a = map(int, str(num)[1:])
    b = map(int, str(num)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))


resultado = numero_step(numero)

if resultado:
    print("es un numero step")
else:
    print("no es un numero step")
