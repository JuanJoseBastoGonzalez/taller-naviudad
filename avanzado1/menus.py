import os 
jugadores = {}
jugadores ={
    "id":[],
    "nombre":[],
    "partidos jugados":[],
    "partidos gandos":[],
    "puntos a favor":[],
    "total puntos":[]
}

jugadores[123] = {'nombre': 'variable con el nombre', 'edad': 'edad'}
categorias ={
    "novato":[],
    "intermdio":[],
    "avanzado":[]
    }
def menu_principal():
    global opcion
    os.system("cls")
    title="""
    *****************************
    *        MENU PRINCIPAL     *
    *****************************
    """
    print(title)
   
    print("1.registrar jugador.") 
    print("2.registrar partido.")
    print("3.informe ganador actual.")  
    print("4.salir")
    try:
        opcion = int(input("Ingrse una opcion  :"))
        while not (1<= opcion <=4):
            print("caracter fuera del rango permitido") 
            opcion = int(input("Ingrse una opcion \n:"))
    except ValueError:
        print("Solo se permitenvalores numericos")
    return opcion



def regitrasj():
    os.system("cls")
    titulur = """
    ************************************
    *       REGISTRO DE JUGADORES      *
    ************************************
    """

    print(titulur)
    for i in range(0,1):
        registrar_id = input("Ingrese el ID del jugador que desea registrar  \n:")
        if registrar_id in jugadores["id"]:
            print("El jugador ya ha sido registrado")
            break
        else:
            jugadores["id"].append(registrar_id)
            print("Jugador registrado exitosamente")
        registrar_n = input("Ingrse el nombre del jugador que desea registrar  \n:")
        jugadores["nombre"].append(registrar_n)
        try:
            categoria  = int(input("Ingrese la edad del jugador \n:"))
        except ValueError:
            print("Solo se permiten valores numericos ")    
        if categoria <14:
            print(f"No hay categorias disponibles para el jugador {registrar_n} ")
            break      
        elif (15 <= categoria <=16):     
            categorias["novato"].append(registrar_id)
        elif (17 <= categoria <=20):
            categorias["intermdio"].append(registrar_id)
        else:
            if categoria> 20:
                categorias["avanzado"].append(registrar_id)
        os.system("cls")
        jugadores["partidos jugados"].append([])
        jugadores["partidos gandos"].append([])
        jugadores["puntos a favor"].append([])
        jugadores["total puntos"].append([])
        print(jugadores["id"])
        print(jugadores["nombre"])
        print(categorias["novato"])
        print(categorias["intermdio"])
        print(categorias["avanzado"])
        print(jugadores["partidos jugados"])
        print(jugadores["partidos gandos"])
        print(jugadores["puntos a favor"])
        print(jugadores["total puntos"])
        
        i +=1

def regitrarps ():
    os.system("cls")
    titulop="""
    ************************************
    *       REGISTRO DE PARTIDOS      *
    ************************************
    """
    print(titulop)
    partido_id =input("Ingrese el id del jugador \n:")
    if partido_id not in jugadores["id"]:
        print("El jugador no esta registrado")
        try:
            registrar = input("Desea registrar al jugador? [S][N] \n:").upper()
            while registrar !="S" and registrar !="N":
                registrar = input("Desea registrar al jugador? [S][N] \n:").upper()
        except ValueError:
            print("opcion no valida")
            
        if registrar =="S":
            regitrasj()
        else:
            pass
    else:
        try:
            partido = int(input("Ingrse la cantidad de partidos jugados \n:" ))
        except ValueError:
            print("caracter no valido")
       
        else:
            os.system("cls")
            print(jugadores["partidos jugados"])
            for i in range(partido):
                pts_jugador =int(input(f"ingrese los puntos realizar en el partido #{i+1} \n:"))
                pts_rival= int(input(f"ingrese los puntos que el contrincante le realizo en el partido #{i+1} \n:"))
                pts_Afavor = int(pts_jugador - pts_rival)
                if pts_Afavor <0:
                    pts_Afavor = 0  
                else:
                    jugadores["puntos a favor"][jugadores["id"].index(partido_id)].append(pts_Afavor)
                if pts_rival > pts_jugador:
                    jugadores["partidos gandos"][jugadores["id"].index(partido_id)].append(0)
                else:
                    if pts_jugador == pts_rival:
                        pass
                    else:
                        jugadores["partidos gandos"][jugadores["id"].index(partido_id)].append(2)
                print(jugadores)
                i+=1
                print(jugadores["id"])
                print(jugadores["nombre"])
                print(categorias["novato"])
                print(categorias["intermdio"])
                print(categorias["avanzado"])
                print(jugadores["partidos jugados"])
                print(jugadores["partidos gandos"])
                print(jugadores["puntos a favor"])
                print(jugadores["total puntos"])
                os.system("pause")
                os.system("cls")
   
def ganador():
    os.system("cls")
    title = """
    ********************************
    *         EL GANADOR  ES       *
    ********************************
    """
    print(title)
    orden = list(jugadores["partidos gandos"])
    #novato
    # for i in categorias["novato"]:
    #     for j in  jugadores["id"].index(i):
    #         contador = jugadores["id"].index(j) 
    #         for contador in jugadores["partidos gandos"]:
    ganadorj=[]
    #for i in range(len(categorias["novato"][i])):
    for h in categorias["novato"]: 
            indx = jugadores["id"].index(h)
            ganadorj.append( jugadores["partidos gandos"][indx])
    
    gandorf = max(ganadorj)
    indx= jugadores["partidos gandos"].index(ganadorj)
    print("CATEGORIA NOVATO")
    print(jugadores["nombre"][indx])
    print(gandorf)
    os.system("pause")

