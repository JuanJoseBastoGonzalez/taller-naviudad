dias, A, M, D = 0, 0, 0, 0
print("INGRESE CANTIDAD DE DÍAS:")
dias = int(input())
A = dias // 365
M = (dias - (A * 365)) // 30
D = dias - ((A * 365) + (M * 30))
print("Años:", A)
print("Meses:", M)
print("Días:", D)
