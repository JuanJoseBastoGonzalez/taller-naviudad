

nombres_ciudades = []
datos_ciudades = []
informe= [0,0,0,0,0]
import menu
import os 
def registrar_ciudad():
    if len(nombres_ciudades) < 5:
        try:
         nombre_ciudad = input("Ingrese el nombre de la ciudad: ").upper()
        except ValueError:
            print("Caracter invalido")
        while nombre_ciudad in nombres_ciudades:    
            print("ciudad ya registrada incerte el nombre de una ciudad que no este registrada")
            nombre_ciudad = input("Ingrese el nombre de la ciudad: ").upper()
        nombres_ciudades.append(nombre_ciudad)
        datos_ciudades.append([])
    else:
         print("solo se permiten 5 ciudades")
    print(nombres_ciudades)
    
    
    
    
def registrar_sismo():
    global magnitud_sismo
    nombre_ciudad = input("Ingrese el nombre de la ciudad para el registro del sismo: ").upper()
    if nombre_ciudad in nombres_ciudades:
        while True:
            try:
                magnitud_sismo = float(input("Ingrese la magnitud del sismo: "))
                break
            except ValueError:
                print("Caracter invlaido solo se permiten numeros")
        indice_ciudad = nombres_ciudades.index(nombre_ciudad)
        datos_ciudades[indice_ciudad].append(magnitud_sismo)
        print(f"Sismo registrado en {nombre_ciudad}: {magnitud_sismo}")
    else:
        print(f"La ciudad {nombre_ciudad} no está registrada. Debe registrar la ciudad primero.")
        registrar_city = input("Desea registrar una ciudad").upper() 
        if registrar_city == "SI":
            registrar_ciudad()
        else:
            menu.opcinesMenu()
    print(nombres_ciudades)
    print(datos_ciudades)

    
def buscar_ciudades():
    nombre_ciudad = input("Ingrese el nombre de la ciudad que desea buscar").upper()
    if nombre_ciudad in nombres_ciudades:
        indice_ciudad = nombres_ciudades.index(nombre_ciudad)
        print(nombre_ciudad)
        print(datos_ciudades[indice_ciudad])
    else:
        print(f"La ciudad {nombre_ciudad} no está registrada. Debe registrar la ciudad primero.")
        registrar_city = input("Desea registrar una ciudad").upper() 
        if registrar_city == "SI":
            registrar_ciudad()
        else:
            menu.opcinesMenu()
      
        



def informe_riezgo():
    informes=[]
    fin=[]
    datos= list(datos_ciudades)
    # a =    len(datos[0])
    # b=    len(datos[1])
    # c=   len(datos[2])
    # d=    len(datos[3])
    # e=    len(datos[4])
    
    # print(datos)
    # fin.extend([a,b,c,d,e])
    # fin2 = list(fin)
    # fin2.sort()
    # if  fin2[0] != fin2[4]:
    try:
      if a != b or a != c or a != d or a != e:
        print("hay ciudades a las que les fantan dtos de sismos porfavor corregir")
        registrar_sismo()
      else:
        a =  len(datos[0])
        b=   len(datos[1])
        c=   len(datos[2])
        d=   len(datos[3])
        e=   len(datos[4])
    # try:
        informe[0] = sum(datos_ciudades[0])
        print(informe[0])
        informe[1] = sum(datos_ciudades[1])
        print(informe[1])
        informe[2] = sum(datos_ciudades[2])
        print(informe[2])
        informe[3] = sum(datos_ciudades[3])
        print(informe[3])
        informe[4] = sum(datos_ciudades[4])
        print(informe[4])
    except IndexError:
        print("favor incerte las ciudades faltantes para poder precentar un informe completo")
        repetir =5- len(nombres_ciudades)
        if len(nombres_ciudades) < 5:    
            while repetir != 0:
                repetir = len(nombres_ciudades) -5#revisar bucle 
                registrar_ciudad()
                repetir = len(nombres_ciudades) -5
    
   
        
    
    
            # menu.opcinesMenu()
    os.system("pause")  
    for i in range(0,4):  
        informes.append(informe[i])#revisar typeError
    os.system("pause")
    informes.sort()
    print(informes)



def salir():
    global confirmacion
    confirmacion = input("¿Está seguro de salir? [SI][NO]").upper()
    while confirmacion not in ["SI", "NO"]:
        print("Respuesta inválida. Por favor, responda [SI] o [NO].")
        confirmacion = input("¿Está seguro de salir? [SI][NO]").upper()
    return confirmacion
 

        
        
