import titulos#titulos y menus
import os 
def menu_inicio():
    titulos.inicio_titulo()
    os.system('pause')
    isActive = True
    while isActive:
        try:
            opmenu=int(input(f"{titulos.menu_inicio()}  \nIngrese una opcion :"))
            while (0 > opmenu ) or opmenu >6: 
                print("seleccino fuera del rango permitida")           
                os.system('pause & cls')
                opmenu=int(input(f"{titulos.menu_inicio()} \nIngrese una opcion :"))
        except ValueError:
            print("Opcion no valida solo se permiten numeros")
            os.system('pause & cls')
        else:
            isActive = False
    os.system('cls')
    return opmenu
def menu_rutas():
    titulos.rutas_titulo()
    os.system('pause')
    isActive = True
    while isActive:
        try:
            opmenu=int(input(f"{titulos.rutas_menu()}  \nIngrese una opcion :"))
            while (0 > opmenu ) or opmenu >2: 
                print("seleccino fuera del rango permitida")           
                os.system('pause & cls')
                opmenu=int(input(f"{titulos.rutas_menu()} \nIngrese una opcion :"))
        except ValueError:
            print("Opcion no valida solo se permiten numeros")
            os.system('pause & cls')
        else:
            isActive = False
    os.system('cls')
    return opmenu
def agregar_Ruta():
    titulos.rutas_titulo()
    # os.system('pause')
    isActive = True
    while isActive:
        try:
            opmenu= input("Desea gregar una nueva ruta? [S][N]").upper()
            while opmenu  !="S" and opmenu!="N": 
                print("seleccino fuera del rango permitida")           
                os.system('pause & cls')
                opmenu= input("Desea gregar una nueva ruta? [S][N]").upper()
        except ValueError:
            print("Opcion no valida ")
            os.system('pause & cls')
        else:
            isActive = False
    os.system('cls')
    return opmenu
def agregar_notas():
    titulos.notas_titulo()
    # os.system('pause')
    isActive = True
    while isActive:
        try:
            opmenu= int(input("ingrese la nota del camper"))
            while opmenu =="0": 
                print("seleccino fuera del rango permitida")           
                os.system('pause & cls')
                opmenu= int(input("ingrese la nota del camper"))
        except ValueError:
            print("Opcion no valida ")
            os.system('pause & cls')
        else:
            isActive = False
    os.system('cls')
    return str(opmenu)
# def salones():
#     os.system('cls')
#     titulos.salones()
#     isActive = True
#     while isActive:
#         try:
#             opmenu= int(input("1. Ver salones \n2. Agregar salon")).upper()
#             while opmenu  !=1 and opmenu!=2: 
#                 print("seleccino fuera del rango permitida")           
#                 os.system('pause & cls')
#                 opmenu= int(input("1. Ver salones \n2. Agregar salon")).upper()
#         except ValueError:
#             print("Opcion no valida ")
#             os.system('pause & cls')
#         else:
#             isActive = False
#     os.system('cls')
    # return opmenu

    
    
   
    