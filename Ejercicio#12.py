class Nomina:

    @staticmethod
    def calcular_salario_bruto(horas_trabajadas, valor_hora):
        return horas_trabajadas * valor_hora

    @staticmethod
    def calcular_valor_retefuente(porcentaje_retefuente, salario_bruto):
        return porcentaje_retefuente * salario_bruto

    @staticmethod
    def calcular_salario_neto(salario_bruto, valor_retefuente):
        return salario_bruto - valor_retefuente


# Datos del problema
horas_trabajadas = 48
valor_hora = 5000
retencion = 12.5

# Conversión del porcentaje
porcentaje_retefuente = retencion / 100

# Cálculos usando la clase Nomina
salario_bruto = Nomina.calcular_salario_bruto(horas_trabajadas, valor_hora)
valor_retefuente = Nomina.calcular_valor_retefuente(porcentaje_retefuente, salario_bruto)
salario_neto = Nomina.calcular_salario_neto(salario_bruto, valor_retefuente)

# Impresión de resultados
print(f"Salario Bruto: {salario_bruto}")
print(f"Retención en la Fuente: {valor_retefuente}")
print(f"Salario Neto: {salario_neto}")