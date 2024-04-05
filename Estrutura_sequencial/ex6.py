import math

def calcular_area_circulo(raio):
    if raio < 0:
        return "Raio não pode ser negativo"
    else:
        return math.pi * raio ** 2

raio = float(input("Digite o raio do círculo: "))
area = calcular_area_circulo(raio)
print("A área do círculo é:", area)
