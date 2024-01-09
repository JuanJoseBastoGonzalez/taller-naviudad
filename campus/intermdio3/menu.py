
def opcinesMenu():
    global opmenu
    print("1.Registrar ciudad..........")
    print("2.Registrar sismo...........")
    print("3.Buscar sismo por ciudad...")
    print("4.Informe de riezgo.........")
    print("5.Salir.....................")
    try: 
        opmenu = int(input("Seleccione una opcion"))
    except ValueError:
        print("Carcter incalido")
    while opmenu not in  range(1,6):
        print("valor fuera del rango")
        opmenu = int(input("Seleccione una opcion"))
    return opmenu