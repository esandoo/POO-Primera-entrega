class Edades:

    @staticmethod
    def calcular_edalber(edjuan):
        return (2 * edjuan) / 3

    @staticmethod
    def calcular_edana(edjuan):
        return (4 * edjuan) / 3

    @staticmethod
    def calcular_edmama(edjuan, edalber, edana):
        return edjuan + edalber + edana


# Caso específico
edjuan = 9
edalber = Edades.calcular_edalber(edjuan)
edana = Edades.calcular_edana(edjuan)
edmama = Edades.calcular_edmama(edjuan, edalber, edana)

print("ALBERTO:", edalber)
print("JUAN:", edjuan)
print("ANA:", edana)
print("MAMÁ:", edmama)