class Potencias:

    @staticmethod
    def calcular_cuadrado(numero):
        return numero ** 2

    @staticmethod
    def calcular_cubo(numero):
        return numero ** 3

"""""
numero = float(input("Ingrese un número: "))

Esta es la forma general, pero en la clase trabajamos con el caso nuemero = 4.0

"""
numero = 4.0

# Cálculos usando la clase
cuadrado = Potencias.calcular_cuadrado(numero)
cubo = Potencias.calcular_cubo(numero)

# Impresión de resultados
print(f"Número ingresado: {numero}")
print(f"Cuadrado: {cuadrado}")
print(f"Cubo: {cubo}")