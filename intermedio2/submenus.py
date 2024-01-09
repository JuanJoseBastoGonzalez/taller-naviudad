import os 
menude_pendencias=["consumo electrónico","Consumo de transporte"]
def menu_consumo_tipo():
    isActive= True
    while isActive:
        try:
            tipo_consumo =int(input("ingrse el tipo de consumo que desea registrar :"))
            while not (1<= tipo_consumo <=2):
                print("opcion invalida")
                tipo_consumo =int(input("ingrse el tipo de consumo que desea registrar :"))
        except ValueError:
            print("opcion invalida")
        else:
            isActive = False
    os.system("cls")
    return  int(tipo_consumo)
def consumo_electrico():
    imprimir=["\t CONSUMO ELECTRONICO ","1. Consumo por electrodomestico ","2. Consumo por factura"]
    for i in range(1,3):
            print(imprimir[i])
    isActive = True
    while isActive:
        try:
            op_electronico = int(input("Seleccione una opcion  :"))
            while not (1<= op_electronico <=2):
                print("Opcion no vlaida")
                op_electronico = int(input("Seleccione una opcion  :"))
        except ValueError:
            print("caracter no valido")
        else:
            isActive = False      
    os.system("cls")  
    return int(op_electronico)
def consumo_equipos():
    isActive = True
    while isActive:
        try:
            potencia = float(input("Ingrese la potencia en Waths del dispositivo"))
            while potencia <=0:
                print("la potencia no peude ser mennor a 0")
                potencia = float(input("Ingrese la potencia en Waths del dispositivo"))
        except ValueError:
            print("caracter no valido")
        else:
            isActive = False  
    isActive = True
    while isActive:
        try:
            horas_uso = float(input("Ingrese las horas de uso del dispositivo"))
            while horas_uso<0:
                print("las horas de uso no peude ser menor a") 
                horas_uso = float(input("Ingrese las horas de uso del dispositivo"))
        except ValueError:
            print("caracter no valido")
        else:
            isActive = False   
    consumo_dispositivo = ((horas_uso*potencia)/1000)*0.5
    return int(consumo_dispositivo)
def consumo_electrco_factura1():
    print("1. Factura Semestral \n2. Factura anual")          
    isActive = True
    while isActive:
        try:
            factura_tipo = int(input("Ingrese una opcion"))
            while not (1<= factura_tipo <=2):
                print("Opcion no valida")
                factura_tipo = int(input("Ingrese una opcion")) 
        except ValueError:
            print("Opcion no valida")
        else:
            isActive = False 
    return int(factura_tipo)
def consumo_electrco_factura2():
    isActive = True
    while isActive:
        try:
            consumo_faturaA =float(input("ingrese el consumo de su factora anual"))
            while consumo_faturaA < 0:
                print("el valor del consumo debe ser superior o igual a 0")
                consumo_faturaA =float(input("ingrese el consumo de su factora anual"))
        except ValueError:
            print("caracter no valido")
        else:
            isActive = False    
    return float(consumo_faturaA)
def consumo_transporte_co2():
    isActive = True
    while isActive:
        try:
            consumo_transporte = float(input("Ingrese la cantidad de kilometros recorridos en  vehiculos a combustioon"))
            while consumo_transporte <0:
                print("el consumo debede ser igual o mayor a 0")
                consumo_transporte = float(input("Ingrese la cantidad de kilometros recorridos en  vehiculos a combustioon"))
        except ValueError:
            print("caracter no valido")
        else:
            isActive = False
    return float(consumo_transporte)
def  consumo_mensual():
    isActive = True
    while isActive:
        try:
            consumo_factura = float(input("Ingrse su consumo mensual"))
        except ValueError: 
            print("caracter no valido")
        else:
            isActive = False
    return float(consumo_factura)
   
    