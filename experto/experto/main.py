import json
import funciones.campers as c
import menus 
import os
# import funciones.corefile as core
campus={
    "campus":{
        "campers":{},
        "rutas":{},
        "pruevas":{},
        "salones":{},
    }
}
with open('campus.json','w')as cam:
    json.dump(campus,cam,indent=4)
# MY_DATABASE:/"data/"
def inicio():
    op_menu_ini=menus.menu_inicio()
    # core.NewFile()
    if op_menu_ini ==1:
            campus.get(c.NewCamper(campus))
            # param= campus
            # core.AddData(*param)
            print(json.dumps(campus,indent=4))
            os.system('pause & cls')
            inicio() 
            with open('campus.json','w')as cam:
                json.dump(campus,cam,indent=4) 
            print(json.dumps(campus,indent=4))    
    if op_menu_ini ==2:
        op_rutas=menus.menu_rutas()
        if op_rutas ==1:
            print(campus["campus"]["rutas"])
            os.system('pause & cls')
            inicio()
        else:
            while menus.agregar_Ruta() == "S":# print( campus.get(c.NewRuta(campus)))
                campus.get(c.NewRuta(campus))
                print(json.dumps(campus,indent=4))
                os.system('pause & cls')
                with open('campus.json','w')as cam:
                     json.dump(campus,cam,indent=4)
            inicio()
    if op_menu_ini ==3:
         #if op_menu_sal==1:        
        campus.get(c.SalonAgregar(campus))
        print(json.dumps(campus,indent=4))
        os.system('pause & cls')
        with open('campus.json','w')as cam:
            json.dump(campus,cam,indent=4)
        inicio()
        #else:
                 #salones
    #     campus.get(c.Salones(campus))
    #     with open('campus.json','w')as cam:
    #         json.dump(campus,cam,indent=4)
    if op_menu_ini ==4:
        campus.get(c.Notas(campus))
        print(json.dumps(campus,indent=4))
        os.system('pause & cls')
        with open('campus.json','w')as cam:
            json.dump(campus,cam,indent=4)
        inicio()
        
if __name__ ==  '__main__':
    inicio()

        
    

    