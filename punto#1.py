#Definir los métodos para inicializar sus atributos

print (" ")
print ("Torres Olvera Gael")
print (" ")

#declarando variable
class Estudiante():
    def __init__(self , nom , Calificacion):
        self.nom=nom
        self.Calificacion=Calificacion

#Iniciando funcion def
    def imprimir(self):
        print (f"Alumno:{self.nom} \nCalificacion: {self.Calificacion}")

    def resultados(self):
        if self.Calificacion >= 6:
            print("Has aprobado! (;")
        else:
            print("Has reprobado! ):")

#resultados
e1=Estudiante(str(input("Ingresa tu nombre: ")) , float(input("Ingresa tu Calificacion : ")))
e1.imprimir()
e1.resultados()

e2=Estudiante(str(input("Ingresa tu nombre: ")) , float(input("Ingresa tu Calificacion : ")))
e2.imprimir()
e2.resultados()


