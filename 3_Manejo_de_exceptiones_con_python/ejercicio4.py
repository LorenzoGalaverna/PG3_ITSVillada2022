while True:
    try:
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))
        print("el resultado de la division de los numeros es: ", numero1 / numero2)
        decision = input("desea continuar? (si/no): ")
        if decision == "si":
            continue
        elif decision == "no":
            break
        else:
            print("ingrese una opcion valida")
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
    except ValueError:
        print("ingrese un valor correcto")
