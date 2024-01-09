import json
import funciones.campers as c 

campus ={
    "campus":{
        "campers":{},
        "rutas":{},
        "pruevas":{},
         "salones":{},
        "campers":{}
    }
}
if __name__=="__main__":
    c.NewCamper(campus)
    print(json.dumps(campus,indent=4))