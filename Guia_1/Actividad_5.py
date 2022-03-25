palabra = input("Escribe una palabra para averiguar si su palabra es palindromo: ")


def capicua_o_no(palabra_capicua_o_no):
    """Toma una palabra y devuelve si es capicua o no"""

    for i in range(0, int(len(palabra_capicua_o_no) / 2)):
        if (
            palabra_capicua_o_no[i]
            != palabra_capicua_o_no[len(palabra_capicua_o_no) - i - 1]
        ):
            return False
    return True


resultado = capicua_o_no(palabra)

if resultado:
    print("La palabra es palindromo")
else:
    print("La palabra no es palindromo")
