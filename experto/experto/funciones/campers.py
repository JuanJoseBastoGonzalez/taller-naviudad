import funciones.corefile as cf 
import json
import os 
import titulos 
import menus
cf.MY_DATABASE='data/campers.json'
def NewCamper(campus: dict):
    global siguiente_numero
    global id
    siguiente_numero=0
    data= campus.get("campus").get("campers")
    camper={
      
        "Numero ID":"",
        "Nombre":'',
        "Apellido":'',
        "Direccion":'',
        "Acudiente":{}, 
        "Telcontacto":{},
        "Estado":''
    }
    acudiente={
        "id":'',
        "nrotel":'',
        "nombre":'',
        "email":'',
    }
    phone={
    "id":"",
    "nrotel":"",
    "ubicaion":""
    }
    j=0
    titulos.datos_titulo()
    for i in camper:
        if (0<j <4):
            nuevo_camper= input(f"Ingrese el {i} del camper ")
            camper[i]=nuevo_camper
        j+=1
    os.system('cls')
    titulos.datos_titulo()
    for i in acudiente:
        nuevo_camper= input(f"Ingrese el {i} del acudiente del camer {camper['Nombre']} ")
        acudiente[i]=nuevo_camper
    os.system('cls')
    for i  in phone:
        titulos.datos_titulo
        nuevo_camper= input(f"Ingrese el {i} del acudiente del camer {camper['Nombre']} ")
        phone[i]= nuevo_camper
    camper["Acudiente"]=acudiente
    camper["Telcontacto"]= phone
    data["campers"]=camper 
    contador = 0 
    contador +=1 
    if contador:
        siguiente_numero1 =  contador
    else:
        siguiente_numero1 = "001" 
    data[siguiente_numero1]=camper
rutas={}
def NewRuta(campus : dict):
    datar = campus.get("campus").get("rutas")
    rutas = input("Escriba el nombre de la nueva ruta: ")
    claves = datar.keys()
    if claves:
        siguiente_numero = str(int(max(claves)) + 1).zfill(3)  
    else:
        siguiente_numero = "001" 
    datar[siguiente_numero] = rutas
pruevas1={}   
def NewPruevas(campus : dict):
    datap = campus.get("campus").get("pruevas")
    pruevasAdd = input("DIjite el Id del alumno")
    pruevas1.append(pruevasAdd)
    pruevasAdd = input("ingrese  la nota de la prueva teorica ")
    pruevas1.append(pruevasAdd)
    pruevasAdd = input("ingrese  la nota de la prueva practica ")
    pruevas1.append(pruevasAdd)
    claves = datap.keys()
    if claves:
        siguiente_numero = str(int(max(claves)) + 1).zfill(3)  
    else:
        siguiente_numero = "001" 
    datap[siguiente_numero] = pruevas1
# def Salones(campus : dict):
#     menus.salones()
#     salonver= campus.get("campus").get("salones")
#     claves = salonver.keys()
#     if claves:
#         siguiente_numero = str(int(max(claves)) + 1).zfill(3)  # Incremento automático
#     else:
#         siguiente_numero = "001" 
    
#     salonver[siguiente_numero]=Salones
def SalonAgregar(campus : dict):
    titulos.salones_titulo()#pasar liena  menus 
    datasal= campus.get("campus").get("salones")
    salon = input("Escriba el nombre del salon  ")
    claves = datasal.keys()
    if claves:
        siguiente_numero = str(int(max(claves)) + 1).zfill(3)  
    else:
        siguiente_numero = "001" 
    datasal[siguiente_numero] = salon
def Notas(campus : dict):
    datanota= campus.get("campus").get("pruevas")
    nota= menus.agregar_notas()
    claves = datanota.keys()
    if claves:
        siguiente_numero = str(int(max(claves)) + 1).zfill(3)  
    else:
        siguiente_numero = "001" 
    datanota[siguiente_numero] = nota