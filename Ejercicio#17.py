import math

class Circulo:

    @staticmethod
    def calcular_area(radio):
        return math.pi * math.pow(radio,2)

    @staticmethod
    def calcular_longitud(radio):
        return 2 * math.pi * radio


# radio = float(input("Ingrese el radio del círculo: ")) Forma general
radio = 3  # Caso fijo para prueba tratado enclase 

area = Circulo.calcular_area(radio)
longitud = Circulo.calcular_longitud(radio)

print(f"Longitud de la circunferencia: {longitud}")
print(f"Área del círculo: {area}")
