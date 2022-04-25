class Persona:

    def inicializar(self, name):
        self.nombre = name

    def imprimir (self):
        print("nombre: ", self.nombre)


persona1 = Persona()
nombre1 = input ("ingrese el nombre de la persona")
persona1.inicializar(nombre1)
persona1.imprimir()

persona2 = Persona()
nombre2 = input ("ingrese el nombre de la persona")
persona2.inicializar(nombre2)
persona2.imprimir()