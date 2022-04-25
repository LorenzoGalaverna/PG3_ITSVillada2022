class Familia:
    def __init__(self):
        self.nombre_madre = input("ingrese el nombre de la madre ")
        self.nombre_padre = input("ingrese el nombre del padre ")
        self.hijos = input("ingrese el nombre de los hijos separados por un espacio ").split()

    def __str__(self):
        respuesta = self.nombre_madre + ", " + self.nombre_padre
        for x in self.hijos:
            respuesta = respuesta + ", " + x
        return respuesta

familia1 = Familia()

print(familia1)

