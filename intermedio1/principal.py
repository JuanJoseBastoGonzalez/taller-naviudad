import menu
import opcines
nombres_ciudades = []
datos_ciudades = []

def menuPricipal():
    global opmenu
    global isActive
    isActive = True
    opmenus = 0
    while isActive:
        opmenus = menu.opcinesMenu()    
        if  opmenus == 1:
            opcines.registrar_ciudad()
            menuPricipal()
        elif opmenus == 2:
           opcines.registrar_sismo()
        elif opmenus == 3:
            opcines.buscar_ciudades()
        elif opmenus == 4:
            opcines.informe_riezgo()
        elif opmenus == 5:
            if opcines.salir() == "SI":
                    isActive = False
            else:
                    isActive = True
    
menuPricipal()



#