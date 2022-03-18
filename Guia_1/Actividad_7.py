numero = int(input("Escribe un numero para averiguar si es step: ")) 
num = [int(i) for i in str(numero)]


def numero_step(num):
    for i in range(0, num(len(num))):
        if num[i] != num[i + 1] :
            return False
    return True
    

resultado = numero_step(num)

if (resultado):
        print("es un numero step")
else:
        print("no es un numero step")