Alto= int(input("ingrese el alto del rectangulo que quiere formar: "))
Ancho= int(input("ingrese el ancho del rectangulo que quiere formar: "))
Caracter= input("ingrese el caracter que quiere usar para formar el rectangulo: ")

def formar_rectangulo(altura,anchura,Caracter):
    for y in range(altura):
        for x in range(anchura):
            print(Caracter,end="")
        print("")

formar_rectangulo(Alto,Ancho,Caracter)