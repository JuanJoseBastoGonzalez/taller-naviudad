def dependencia_existencia():
    opdepen = input("No existe una dependencia con ese nombre desea registrala?  : [S][N]").upper()
    while opdepen not in ["S","N"]:
        print("Opción inválida. ")
        opdepen = input(" desea registrar una dependencia nueva?  : [S][N]").upper()
    return opdepen   
def rango ():
    isActive= True
    while isActive:
        try:
            op_menu = int(input("Elija una opción: "))
            while op_menu not in range(1, 6):
                print("Opción inválida. ")
        except ValueError:
            print("Opción inválida. ")
        else: 
            isActive = False  
    return int(op_menu)