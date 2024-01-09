num_hijos = 0
dias_no_laborables = 0
SueldoBase = 0.0
sueldo_final = 0.0
print("CALCULAR EL SUELDO FINAL DE UN EMPLEADO")
SueldoBase = float(input("Ingrese Sueldo Base: "))
num_hijos = int(input("Ingresar Numero de Hijos: "))
dias_no_laborables = int(input("Ingresar Dias no Laborables Trabajados: "))
sueldo_final = SueldoBase + (num_hijos * 100) + (dias_no_laborables * 25)
print("\nSUELDO FINAL:", sueldo_final)
