
jugadores ={
    "id":[],
    "nombre":[],
    "partidos jugados":[],
    "partidos gandos":[],
    "puntos a favor":[],
    "total puntos":[]
}
categorias ={
    "novato":[],
    "intermdio":[],
    "avanzado":[]
    }
def menu_principal():
    print ("\tmenu Principal")
    print("1.registrar jugador.") 
    print("2.registrar partido.")
    print("3.informe ganador actual.")
    try:
        opcion = int(input("Ingrse una opcion"))
        while not (1<= opcion <=3):
            print("caracter fuera del rango permitido") 
            opcion = int(input("Ingrse una opcion"))
    except ValueError:
        print("Solo se permitenvalores numericos")
    return opcion



def regitrasj():
    for i in range(0,1):
        registrar_id = input("Ingrese el ID del jugador que desea registrar: ")
        if registrar_id in jugadores["id"]:
            print("El jugador ya ha sido registrado")
            break
        else:
            jugadores["id"].append(registrar_id)
            print("Jugador registrado exitosamente")
        registrar_n = input("Ingrse el nombre del jugador que desea registrar")
        jugadores["nombre"].append(registrar_n)
        # try:
        #     partido= input("El jugador ya jugo partidos? [S][N]").upper()
        #     while partido !="S" and partido !="N":
        #         print("caracter invalido")
        #         partido= input("El jugador ya jugo partidos? [S][N]").upper()
        # except ValueError: 
        #     print("caracter invlaido")
        # if partido == "S":
        #     regitrarp()
        try:
            categoria  = int(input("Ingrese la edad del jugador "))
        except ValueError:
            print("Solo se permiten valores numericos ")    
        if categoria <14:
            print(f"No hay categorias disponibles para el jugador {registrar_n} ")
            break      
        elif (15 <= categoria <=16):     
            categorias["novato"].append(registrar_id)
        
        # try:
        #     partido= input("El jugador ya jugo partidos? [S][N]").upper()
        #     while partido !="S" and partido !="N":
        #         print("caracter invalido")
        #         partido= input("El jugador ya jugo partidos? [S][N]").upper()
        # except ValueError: 
        #     print("caracter invlaido")
        # if partido == "S":
        #     regitrarps()
        jugadores["partidos jugados"].append([])
        jugadores["partidos gandos"].append([])
        jugadores["puntos a favor"].append([])
        jugadores["total puntos"].append([])
        print(jugadores["id"])
        print(jugadores["nombre"])
        print(categorias["novato"])
        print(jugadores["partidos jugados"])
        print(jugadores["partidos gandos"])
        print(jugadores["puntos a favor"])
        print(jugadores["total puntos"])
        i +=1

def regitrarps ():
    partido_id =input("Ingrese el id del jugador")
    if partido_id not in jugadores["id"]:
        print("El jugador no esta registrado")
        try:
            registrar = input("Desea registrar al jugador? [S][N]").upper()
            while registrar !="S" and registrar !="N":
                registrar = input("Desea registrar al jugador? [S][N]").upper()
        except ValueError:
            print("opcion no valida")
        if registrar =="S":
            regitrasj()
        else:
            pass
    
    
    
    
    
    # identificador = jugadores["id"].index(partido_id)
    # try:
    #     partido = int(input("Ingrse la cantidad de partidos jugados" ))
    # except ValueError:
    #     print("caracter no valido")
    # jugadores["partidos jugados"][identificador] = partido
    # print(jugadores["partidos jugados"])
    
 
    
        
        
        
        
        
def buscar():
    ("ingrse el id del jugador que desea buscar")