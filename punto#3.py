#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__

print (" ")
print ("Torres Olvera Gael")
print (" ")

class Calculadora():
    def __init__(self, num1, num2):
        self._num1=num1
        self._num2=num2

    def suma(self):
        resultado=self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2}={ resultado}")

    def resta(self):
        resultado=self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} – {self._num2}={ resultado}")

    def division(self):
        resultado=self._num1 // self._num2
        print(f"El resultado de la divisón es: {self._num1} // {self._num2}= {resultado}")

    def multiplicacion(self):
        resultado=self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

print ("Suma")
operacion=Calculadora(int(input("Ingresa un numero: ")), int(input("Ingresa un numero: ")))
operacion.suma()
print ("resta")
operacion=Calculadora(int(input("Ingresa un numero: ")), int(input("Ingresa un numero: ")))
operacion.resta()
print ("multiplicacion")
operacion=Calculadora(int(input("Ingresa un numero: ")), int(input("Ingresa un numero: ")))
operacion.division()
print ("Division")
operacion=Calculadora(int(input("Ingresa un numero: ")), int(input("Ingresa un numero: ")))
operacion.multiplicacion()