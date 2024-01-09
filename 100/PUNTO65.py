import math
def calcular_area_volumen_cilindro():
    r = float(input("RADIO: "))
    h = float(input("ALTURA: "))
    a = 2 * math.pi * r * (h + r)
    v = math.pi * (r ** 2) * h
    print(f"AREA TOTAL DEL CILINDRO: {a:.2f} cm²")
    print(f"VOLUMEN DEL CILINDRO: {v:.2f} cm³")
calcular_area_volumen_cilindro()
