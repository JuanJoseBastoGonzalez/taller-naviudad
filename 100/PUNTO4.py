xpro =float(0)
for cont in range(1,6):
    nom= input("ingrese el nombre")
    pro = float(input("ingrese el promedio"))
    if xpro < pro:
        xpro = pro
        xnom = nom
print(f" alumno con mayor nota {xnom}")
print(f"promedio {xpro}")