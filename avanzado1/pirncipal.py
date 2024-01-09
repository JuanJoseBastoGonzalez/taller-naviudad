import menus
import os
def linea():
    op_menu = int(menus.menu_principal())
    if op_menu == 1:
       menus.regitrasj()
       os.system('pause')
       linea()
    elif op_menu == 2:
       menus.regitrarps()
       os.system('pause')
       linea()
    elif op_menu == 3:
        menus.ganador()
        os.system('pause')
        linea()
    else:
        print("gracias por usar nuestros servicios")
       
    
linea()