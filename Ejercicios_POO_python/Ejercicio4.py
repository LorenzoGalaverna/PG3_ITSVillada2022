class Operaciones:
    def __init__(self):
        self.numero1 = int(input("ingrese el primer numero"))
        self.numero2 = int(input("ingrese el segundo numero"))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        print("el resultado de la suma es: ", self.numero1 + self.numero2)

    def resta(self):
        print("el resultado de la resta es: ", self.numero1 - self.numero2)

    def multiplicacion(self):
        print("el resultado de la multiplicacon es: ", self.numero1 * self.numero2)

    def division(self):
        print("el resultado de la diviion es: ", self.numero1 / self.numero2)


operacion1 = Operaciones()
