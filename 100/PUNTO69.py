apro = 0.0
desa = 0.0
porA = 0.0
porD = 0.0
print("MOSTRAR EL PORCENTAJE DE ALUMNOS APROBADOS Y DESAPROBADOS")
print("")
apro = float(input("INGRESE CANTIDAD DE ALUMNOS APROBADOS: "))
desa = float(input("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS: "))
print("")
porA = (apro * 100) / (apro + desa)
porD = (desa * 100) / (apro + desa)
print(f"APROBADOS: {round(porA, 2)}%")
print(f"DESAPROBADOS: {round(porD, 2)}%")
