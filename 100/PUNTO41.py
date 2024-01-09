# Declaracion de variables 
salario = float()
desc = float()
# ENTRADA.
print("INGRESE DINERO : ", end="")
salario = float(input())
# PROCESO.
desc = (salario*0.2)
# SALIDA
print("Descuento del 20% : ",desc)
print("Nuevo Salario : ",(salario-desc))

