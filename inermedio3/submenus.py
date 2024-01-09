import menus
productos_stock= []
detalles = []
producto = []
productos =[]
def sub_menu3 ():
        menu=("1.Stock minimo","2.Stock maximo","3.Stock Actual")
        ubicacion= productos.index(producto)
        op_actualizar = int(input("1.Stock minimo \n2.Stock maximo \n3.Stock Actual"))
        while op_actualizar is not range(0,4):
            print ("caracter fuera  del rango permitido")
            op_actualizar = int(input("1.Stock minimo \n2.Stock maximo \n3.Stock Actual"))
        operacion= input("Desea agregar o quitar productos al stock? [A][D]").upper()
        if operacion == "A":
                cantidad = int(input("Ingrese la cantidad de producto que desea agregar al " + menu[op_actualizar]))
                if op_actualizar == 3:
                    productos_stock[ubicacion][7] += cantidad
                elif op_actualizar == 2:
                    productos_stock[ubicacion][5] += cantidad
                else: 
                    productos_stock[ubicacion][4] += cantidad   
        else:
               if operacion == "D":
                    cantidad = int(input("Ingrese la cantidad de producto que desea agregar al " + menu[op_actualizar]))
                    if op_actualizar == 3:
                        productos_stock[ubicacion][7] -= cantidad
                    elif op_actualizar == 2:
                        productos_stock[ubicacion][5] -= cantidad
                    else: 
                        productos_stock[ubicacion][4] -= cantidad     
        
        
        
        
           
        
        
        # ubicacion= productos.index(producto)
        # op_actualizar = int(input("1.Stock minimo \n2.Stock maximo \n3.Stock Actual"))
        # if op_actualizar ==3:
        #    operacion= input("Desea agregar o quitar productos al stock? [A][D]").upper()
        #    if operacion == "A":
        #         cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock actual"))
        #         productos_stock[ubicacion][7] += cantidad
        #    else:
        #        if operacion == "D":
        #             cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock actual"))
        #             productos_stock[ubicacion][7] -=  cantidad     
        # elif op_actualizar == 2:
        #         operacion= input("Desea agregar o quitar productos al stock maximo? [A][D]").upper()
        #         if operacion == "A":
        #             cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maxino"))
        #             productos_stock[ubicacion][5] += cantidad
        #         else:
        #             if operacion == "D":
        #                 cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maximo"))
        #                 productos_stock[ubicacion][5] -=  cantidad
        # else: 
        #     operacion= input("Desea agregar o quitar productos al stock maximo? [A][D]").upper()
        #     if operacion == "A":
        #         cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maxino"))
        #         productos_stock[ubicacion][4] += cantidad
        #     else:
        #         if operacion == "D":
        #             cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maximo"))
        #             productos_stock[ubicacion][4] -=  cantidad   
            
            
        
        
        # elif op_actualizar == 2:
        #         operacion= input("Desea agregar o quitar productos al stock maximo? [A][D]").upper()
        #         if operacion == "A":
        #             cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maxino"))
        #             productos_stock[ubicacion][5] += cantidad
        #         else:
        #             if operacion == "D":
        #                 cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maximo"))
        #                 productos_stock[ubicacion][5] -=  cantidad
        # else: 
        #     operacion= input("Desea agregar o quitar productos al stock maximo? [A][D]").upper()
        #     if operacion == "A":
        #         cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maxino"))
        #         productos_stock[ubicacion][4] += cantidad
        #     else:
        #         if operacion == "D":
        #             cantidad = int(input("Ingrese la cantidad de producto que desea agregar al stock maximo"))
        #             productos_stock[ubicacion][4] -=  cantidad   
            
            



