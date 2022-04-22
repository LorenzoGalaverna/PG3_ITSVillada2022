class Alumno:

    def inicializar(self, name, note):
        self.nombre = name
        self.nota = note

    def imprimir (self):
        if self.nota >= 6 :
            print("nombre: ", self.nombre, ", Estado: aprovado")
        else :
            print ("nombre: ", self.nombre, ", Estado: desaprovado")


alumno1 = Alumno()
alumno1.inicializar("Jose", 7)
alumno1.imprimir()

alumno2 = Alumno()
alumno2.inicializar("Paula", 4)
alumno2.imprimir()