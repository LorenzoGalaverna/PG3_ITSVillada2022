class Persona:

    def inicializar(self, name):
        self.nombre = name

    def imprimir (self):
        print("nombre: ", self.nombre)


persona1 = Persona()
persona1.inicializar("Jose")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("Paula")
persona2.imprimir()