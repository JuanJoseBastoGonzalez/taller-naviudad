import menus
def linea():
   
    op_menu = menus.menu_principal()
    while not ( 1<= op_menu <=5):
        print("Seleccion fuera rango")
        try:
            op_menu = int(menus.menu_principal())
        except ValueError:
            print("opcion no valida...")   
    if op_menu == 1:
        menus.menu1()
        otrop = input("desea  agregar otro producto? [S][N]").upper()
        while otrop == "S":
            menus.menu1()
            otrop = input("desea  agregar otro producto? [S][N]").upper()
        linea()  
    elif op_menu == 2:
        menus.visualize_product()   
        otrop = input("desea  buscar otro producto? [S][N]").upper()
        while otrop == "S":
            menus.visualize_product()
            otrop = input("desea  buscar otro producto? [S][N]").upper() 
        linea()    
    elif op_menu== 3:
        menus.actualizar_product()
        otrop = input("desea actualizar otro producto? [S][N]").upper()
        while otrop == "S":
            menus.actualizar_product()
            otrop = input("desea  actualizar otro producto? [S][N]").upper()
        linea()
    elif op_menu == 4:
        menus.informe()
        linea()
linea()