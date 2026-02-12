import math

# Definición de variables
suma = 0
x = 20
y = 40

# Cálculos
suma = suma + x

x = x + math.pow(y, 2)

suma = suma + (x / y)

# Impresión de resultados
print(f"El valor de x es : {x}")
print(f"El valor de y es : {y}")
print(f"El valor de la suma es : {suma}")