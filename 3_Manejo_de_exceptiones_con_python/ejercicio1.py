while True:
    try:
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ingrese otro numero: "))
        print("el resultado de la suma de los numeros es: ", numero1 + numero2)
        decision = input("desea continuar? (si/no): ")
        if decision == "si":
            continue
        elif decision == "no":
            break
        else:
            print("ingrese una opcion valida")
    except ValueError:
        print("por favor esciba un numero y no letras u otrosa cosas")
