#Desarrollar un programa con tres clases

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Definiendo variables
class Universidad():
    def __init__(self,Nombre):
        self.Nombre=Nombre

#Definiendo variables
class Carerra():
    def carrera(self,especialidad):
        self.especialidad=especialidad

#Definiendo variables
class Estudiante(Universidad,Carerra):
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en {self.Nombre}")

#Imprimiendo los datos
persona=Estudiante(str(input("Nombre del lugar donde estudias: ")))
persona.carrera(str(input("Ingresa el nombre de la especialidad en la que estas: ")))
persona.datos(str(input("Ingresa tu nombre: ")), int(input("Ingresa tu edad: ")))