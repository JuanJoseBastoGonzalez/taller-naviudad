import submenus 
import menus
import os 
def inicio():
    os.system('cls')
    opmenu = int(menus.menu_principal())
    if opmenu == 1:
        os.system('cls')
        menus.Registrar_depen()
        inicio()
    elif opmenu == 2:
        os.system('cls')
        menus.consumo_depen()
        inicio()
    elif opmenu == 3:
        menus.ver_cos()
        
        os.system('pause')
        inicio()
    elif opmenu == 4:
        menus.mayor_co2()
        inicio()
    else: 
        print("Invalid opmenu")
        
inicio()