anio = int(input("Escribe el anio de el cual desea saber si es biciesto o no: "))


def biciesto_o_no(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("El anio es biciesto")
    else:
        print("El anio no es biciesto")

biciesto_o_no(anio)