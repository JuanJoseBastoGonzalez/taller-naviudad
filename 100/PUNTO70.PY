n1 = 0
n2 = 0
n3 = 0
prom = 0.0
print("Verificar si está aprobado o desaprobado")
n1 = int(input("Ingrese NOTA 01: "))
n2 = int(input("Ingrese NOTA 02: "))
n3 = int(input("Ingrese NOTA 03: "))
prom = (n1 + n2 + n3) / 3
if prom > 10.5:
    print(f"APROBADO con {prom:.2f}")
else:
    print(f"DESAPROBADO con {prom:.2f}")
