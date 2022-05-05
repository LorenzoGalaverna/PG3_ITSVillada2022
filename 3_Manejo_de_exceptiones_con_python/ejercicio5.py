while True:
        try:
            escribir = input("ingrese lo que quiera guardar en el txt: ")
            texto = open('3_Manejo_de_exceptiones_con_python/texto.txt', 'a')

            if escribir.isnumeric():   
                texto.write(int(escribir))
            else:
                texto.write(escribir)

            decision = input("desea continuar? (si/no): ")
            if decision == "si":
                continue   
            elif decision == "no":
                break
            else:
                print("ingrese una opcion valida")
    
        except TypeError:
            print("ingrese un valor que no contenga un numero")