import os
productos_stock= []
detalles = []
producto = []
productos =[]
datos =["codigo del producto","nombre del producto","valor de compra del producto","valor de venta del producto","stock minino","stock maxino","nombre del proveedor","stock"]           
opcciones =["1.Stock minimo \n2.Stock maximo \n3.Stock Actual"]
def menu_principal():
    os.system("cls")
    titulo="""
    *******************************
    *       Menu Principal        *
    *******************************
    """
    print(f"\t{titulo}")
    print("1.Regitro de Productos \n2.Visualizar productos \n3.Actualizar stock \n4.Informe de Productos criticos \n5.Calculo de ganancias")
    op_menu = int(input("Seleccione una opcion"))
    os.system("pause")
    return op_menu
    
def menu1():
    os.system("cls")
    titulo="""
    *************************************
    *       REGISTRO DE PRODUCTOS       *
    *************************************
    """
    print(f"\t {titulo}")
    detalles = [] 
    producto= input(f"ingrese el {datos[0]}")
    while producto in productos:
        print("el producto ya fue registrado con anterioridad")#codigo
        producto= input(f"ingrese el {datos[0]}")
    productos.append(producto)
    os.system("cls")
    
    for i in range(1,2):
        detalles.append(input(f"ingrese el {datos[i]}"))#nombre
    
    for i in range(2,6):#falta Manejo de errores
        isActive = True
        while isActive:
            try:
                numero = float(input(f"Ingrese el {datos[i]} número: "))
                if numero >= 0:
                    break  # Sale del bucle si el número es válido (es un número y es mayor o igual a 0)
                else:
                    print("Error: el inventario debe ser mayor o igual a 0")
            except ValueError:
                print("Error: Carácter inválido, inténtelo nuevamente")
            else:
                isActive = False
        detalles.append(numero)
    os.system("cls")
    
    
    
    
    
    for i in range(6,7):
        detalles.append(input(f"ingrese el {datos[i]} "))      
    for i in range(7,8):
        isActive = True
        while isActive:
            try:   
                numero = (int(input(f"ingrese el {datos[i]} N")))
                while numero < 0:
                    print("Error el inventario veser mayo o igual a 0")
                    numero = (int(input(f"ingrese el {datos[i]} N")))
            except ValueError:
                print("Error caracter invalido, intelo nuevamente") 
            else:
                isActive = False  
        detalles.append(numero)        
    productos_stock.append(detalles)
    print(productos) 
    print(productos_stock) 
    
def visualize_product():
        producto = input("ingrese el producto que desea buscar")
        if producto not in productos:
            print("Producto no encontrado")
            registarv = input("Desea regitrar un prodcto?  [S][N]").upper()
            while registarv !="S" and registarv !="N":
                print("opcion no valida")
                registarv = input("Desea regitrar un prodcto?  [S][N]").upper()
            if registarv =="S":
                menu1()
            else:
                pass
        else:
            buscar = productos.index(producto)
            print(producto) 
            print(productos_stock[buscar])
        
def actualizar_product():
        producto = input("ingrese el producto que desea actualizar")
        if producto not in productos:
            print("Producto no encontrado")
            agregarp = input("Desea agragar un producto? [S][N]").upper()
            while agregarp!="S" and agregarp!="N":
                print("Opcion no valida")
                agregarp = input("Desea agragar un producto? [S][N]").upper()
            os.system("clas")
            os.system("pause")
            if agregarp =="S":
                menu1()
            else:
                pass     
        else:
            menu=("1.Stock minimo","2.Stock maximo","3.Stock Actual")
            ubicacion= productos.index(producto)
            op_actualizar = int(input(opcciones))
            while not (1<= op_actualizar <=3):
                print ("caracter fuera  del rango permitido")
                op_actualizar = int(input(opcciones) )
            os.system("cls")
            operacion= input("Desea agregar o quitar productos al stock? [A][D]").upper()
            if operacion == "A":
                    try:
                        cantidad = int(input("Ingrese la cantidad de producto que desea agregar al " + menu[op_actualizar -1]))
                        while cantidad <0:
                            print ("Cantidad de producto no valida")
                            cantidad = int(input("Ingrese la cantidad de producto que desea agregar al " + menu[op_actualizar -1]))
                    except ValueError:
                        print("Error solo se permiten valores numericos enteros")
                    if op_actualizar == 3:
                        print(productos_stock[ubicacion][6] )
                        os.system("pause")
                        n=productos_stock[ubicacion][6] #######
                        productos_stock[ubicacion][6]=n+cantidad
                    elif op_actualizar == 2:
                        productos_stock[ubicacion][4] += cantidad
                    else: 
                        productos_stock[ubicacion][3] += cantidad   
            else:
                    if operacion == "D":
                        isActive = True
                        while isActive:
                            try:
                                cantidad=  int(input("Ingrese la cantidad de producto que desea quitar al " + menu[op_actualizar -1]))
                            except ValueError:
                                print("Error solo se permiten valores numericos enteros")
                            else:
                                isActive = False
                        if op_actualizar == 3:
                            productos_stock[ubicacion][6] -= cantidad
                        elif op_actualizar == 2:
                            productos_stock[ubicacion][4] -= cantidad
                        else: 
                            productos_stock[ubicacion][3] -= cantidad  
        print(productos_stock)
        
def informe():
    cantidad = len(productos)
    listamod = list(productos_stock)
    for i in range(0,cantidad):
        if listamod[i][6] < listamod[i][3]:
            print("Los productos criticos son")
            print (f"{productos[i]} con un total de {listamod[i][6]} productos en stock ")
            
        else:
            print("no hay productos en estado critico")

def ganancias():
    ganancia =[]
    cantidad = len(productos)
    listamod = list(productos_stock)
    for i in range(0,cantidad):
        numero1 =listamod[i][2]
        numero2 = listamod[i][1]
        cuenta = numero1* listamod[i][8] - numero2* listamod[i][8]
        ganancia.append(cuenta)       
        print(f"ganancia por {productos[i]}") 
    print(sum(ganancia))    