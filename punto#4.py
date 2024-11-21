#Crear una clase “Persona” que sea la clase padre de otra clase “Estudiante”

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definiendo las variables
class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

#Estableciendo la funcion
    def nombre_completo(self):
        print(self.nombre +" "+ self.apellido)

#Solcitando mas datos
class Estudiante(Persona):
    def __init__(self,nom,ape,carr):
        super().__init__(nom,ape)
        self.carrera=carr

#Resultado
    def mostrar_carrera(self):
        print(self.carrera)
