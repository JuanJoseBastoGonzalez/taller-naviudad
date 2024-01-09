import menus

def linea():
   op_menu = int(menus.menu_principal())
   if op_menu == 1:
       menus.regitrasj()
       linea()
   elif op_menu == 2:
       menus.regitrarps()
       linea()
    
linea()