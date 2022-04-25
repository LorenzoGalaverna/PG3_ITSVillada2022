class Persona:
    def __init__(self):
        self.nombre = str(input("ingrese el nombre de la persona "))
        self.edad = int(input("ingrese la edad de la persona"))

    def imprimir(self):
        print("nombre de la persona: ", self.nombre)
        print("edad de la persona: ", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("ingrese el sueldo del empleado"))

    def imprimir(self):
        super().imprimir()
        print("el sueldo del empleado es: ", self.sueldo)

    def impuestos(self):
        if self.sueldo > 3000:
            print("el empleado debe pagar impuestos")
        else:
            print("el empleado no debe pagar impuestos")


persona1 = Persona()
persona1.imprimir()
print("---------------------")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.impuestos()
