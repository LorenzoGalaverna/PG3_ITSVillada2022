while True:
    try:
        meses = (
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre",
        )
        respuesta = int(input("Ingrese el número del mes, del 1 al 12: "))
        print(meses[respuesta - 1])
        respuesta2 = input("desea continuar? (si/no): ")
        if respuesta2 == "si":
            continue
        elif respuesta2 == "no":
            break
        else:
            print("ingrese una opcion valida")

    except IndexError:
        print("los meses van del 1 al 12")
    except ValueError:
        print("ingrese un valor correcto")
