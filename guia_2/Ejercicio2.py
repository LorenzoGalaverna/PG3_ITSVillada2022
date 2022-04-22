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
nombre1 = input ("ingrese el nombre de la persona ")
nota1 = int(input ("ingrese la nota de la persona "))
alumno1.inicializar(nombre1, nota1)
alumno1.imprimir()

alumno2 = Alumno()
nombre2 = input ("ingrese el nombre de la persona ")
nota2 = int(input ("ingrese la nota de la persona "))
alumno2.inicializar(nombre2, nota2)
alumno2.imprimir()