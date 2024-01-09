import funciones.corefile as cf

cf.MY_DATABASE = 'data/campers.json '
def NewCamper(campus : dict):
    data=campus.get("campus").get("campers")
    Camper = {
            "NroId":"",
            "NroId":"",
            "Nombre":"",
            "Apellido":"",
            "Direccion":"",
            "Acudiente" :{},
            "telecontacto" : {},
            "estado":""
    }
    acudiente ={
        "id":"",
        "nrotel":"",
        "nombre":"",
        "email":""
    }
    phone
        
        
        
        

    
    print(data)
    # clientes.update(customer)
    # cf .AddData(customer[ "cc" ], clientes)

