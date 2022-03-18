palabra = input("ingreses una palabra para calcular cuantas vocales tiene: ")
def cant_vocales(string):
    num_vocales = 0
    for char in string:
        if char in "aeiouAEIOU":
           num_vocales = num_vocales+1
    print ("la palabra escrita tiene ", num_vocales, " vocales")

cant_vocales(palabra) 