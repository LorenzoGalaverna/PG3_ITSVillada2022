class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado mayor es el lado 1")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("El lado mayor es el lado 2")
        elif self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("El lado mayor es el lado 3")
        else:
            print("no hay un lado mayor")

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("el triangulo es equilatero")
        else:
            print("el triangulo no es equilatero")


lado1 = input("ingrese la medida del lado 1 ")
lado2 = input("ingrese la medida del lado 2 ")
lado3 = input("ingrese la medida del lado 3 ")
triangulo1 = Triangulo()
triangulo1.inicializar(lado1, lado2, lado3)
triangulo1.lado_mayor()
triangulo1.equilatero()
