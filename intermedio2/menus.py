import os
import validaciones 
import submenus 
import titulos
menuo_pciones =["Registrar Dependencia","Registrar consumo por dependencia ","Ver CO2 producido","Dependencia que produce mayor CO2","Salir"]
menude_pendencias=["consumo electrónico","Consumo de transporte"]
dependencias=[]
consumo_temporal=[]
co2=[]
def menu_principal():
    os.system('cls')
    titulos.menu_principal()
    for i in range(1,6):
        print(f"{i}. {menuo_pciones[i-1]}")
    # isActive= True
    # while isActive:
    #     try:
    #         op_menu = int(input("Elija una opción: "))
    #         while op_menu not in range(1, 6):
    #             print("Opción inválida. ")
    #     except ValueError:
    #         print("Opción inválida. ")
    #     else: 
    #         isActive = False   
    
    op_menu= validaciones.rango()
    os.system('cls')
    return op_menu
def Registrar_depen():
    os.system('cls')
    titulos.registro_dependencia()
    nombred = input("Nombre de la dependencia: ").upper()
    while nombred in dependencias:
        print("Ya existe una dependencia con ese nombre")
        nombred = input("Nombre de la dependencia: ").upper()
    dependencias.append(nombred)
    print(f"Dependencia registrada: {dependencias}")
    os.system('pause')
    co2.append([])
    consumo_temporal.append([])
def otro ():
    print(indice)
def consumo_depen():
    global indice
    os.system('cls')
    titulos.consumo_dependencia()
    nombred = input("Nombre de la dependencia: ").upper()
    while nombred not in dependencias:
        # opdepen = input("No existe una dependencia con ese nombre desea registrala?  : [S][N]").upper()
        # while opdepen not in ["S","N"]:
        #     print("Opción inválida. ")
        #     opdepen = input(" desea registrar una dependencia nueva?  : [S][N]").upper()
        opdepen = validaciones.dependencia_existencia()
        if opdepen == "S":
            os.system('cls')
            Registrar_depen()
        else: 
            os.system('cls')
            nombred = input("Nombre de la dependencia: ").upper()
    os.system('cls')
    indice = dependencias.index(nombred) 
    titulos.sub_menu_electricos()
    tipo_consumo = submenus.menu_consumo_tipo()
    if tipo_consumo == 1:#consumo electrico dos partes
        op_electronico = submenus.consumo_electrico()
        if op_electronico == 1:#consumo electrico por electrodomestico
            a = submenus.consumo_equipos()
            consumo_temporal[indice].append(a)
        else:
            #conusmo electrico por factura  
            os.system("cls")
            factura_tipo = submenus.consumo_electrco_factura1()
            if factura_tipo == 1:  
                consumo_factura=submenus.consumo_mensual()
                consumo_temporal[indice].append(consumo_factura*0.5)
                os.system("cls")
            else:
                consumo_faturaA = submenus.consumo_electrco_factura2()    
                consumo_temporal[indice].append((consumo_faturaA/12)*0.5)
                os.system("cls")
    else:#consumo transportes
        consumo_transporte = submenus.consumo_transporte_co2()  
        consumo_temporal[indice].append(consumo_transporte*0.12)
        print(consumo_temporal)
       #fata que guarde consumo_dispositivo en el index corecto y hacer la parte dos del menu 
    print(indice)
    print(f"Consumo registrado: {nombred}")
    os.system('pause')
    return indice
def ver_cos():
    titulos.ver_co2()
    buscar= input("ingrese la dependencia que desea buscar").upper()
    if buscar  not in  dependencias:
        isActive = True
        while isActive:
            try:
                agregar = input("la dependencia no existe desea agregar una nueva? [S][N]").upper()
                while buscar != "S" and buscar != "N":
                    print("Caracter invalido")
                    agregar = input("agregar una nueva dependencia? [S][N]").upper()
            except ValueError:
                print("Caracter invalido")
            else:
                isActive = False  
        agregar = validaciones.nuevo_registro()  
        if agregar == "S":
            Registrar_depen()
            ver_cos() 
    idx = dependencias.index(buscar)
    co2[idx] = sum(consumo_temporal[idx])
    print(dependencias[idx])
    print(consumo_temporal[idx])
    print(co2[idx])
def mayor_co2():
    titulos.mayor_productor()
    print(type(consumo_temporal))
    print(consumo_temporal)
    mayv= map(float,consumo_temporal)
    a=[]
    for i in range((len(consumo_temporal))):
        co2[i] = sum(consumo_temporal[i])
        
    print(co2)    
    mayorp = max(co2)
    idx= co2.index(mayorp)
    print("╔══════════════════════════════════════════════════════════╗")
    print("║       LA DEPENDENCIA QUE GENERO MAYOR CONTAMINACION FUE  ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"                  \t{dependencias[idx]}                     ")
   