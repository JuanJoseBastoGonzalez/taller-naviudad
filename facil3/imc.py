import os 
alumnos =["nombre","edad","peso","altura"]
def imc():
    return alumnos.peso / (alumnos.altura ** 2) 
def rango():
    if imc > 18.5 and imc < 24.9:
        return "Normal"
    elif imc > 25 and imc < 29.9:
        return "Sobrepeso"
    elif imc > 30 and imc < 34.9:
        return "Obesidad"
    elif imc > 35 and imc < 39.9:
        return "Obesidad 2"
    elif imc > 40:
        return "Obesidad 3"




class Alumnos:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
    def imc(self):
       return self.peso / (self.altura ** 2)  
    def rango(self):
        imc = self.imc()
        if imc > 18.5 and imc < 24.9:
            return "Normal"
        elif imc > 25 and imc < 29.9:
            return "Sobrepeso"
        elif imc > 30 and imc < 34.9:
            return "Obesidad"
        elif imc > 35 and imc < 39.9:
            return "Obesidad 2"
        elif imc > 40:
            return "Obesidad 3"
        
contador=1
contadorImc =[0,0,0,0,0]
while contador < 21:
    titulo="""
    ********************************
    *      CALCULADORA DE IMC      *
    *********************************
    """
    print(titulo)
    for i in range(1,20):
        contador += 1 
        os.system("cls")
        nombre = input(f"Ingrese el nombre del alumno # {i} ").upper()
        nombreNumeros = any(caracter.isdigit() for caracter in nombre)
        while nombreNumeros:
            print("El nombre no puede contener números")
            nombre = input("Ingrese el nombre del alumno: ").upper()
            nombreNumeros = any(caracter.isdigit() for caracter in nombre)
        isActive = True
        while isActive:    
            try:
                edad = float(input("Ingrese la edad del alumno en años: "))
                while edad <= 0:
                    print("La edad no puede ser negativa ni 0")
                    edad = float(input("Ingrese la edad del alumno en años: "))
            except ValueError:
                os.system("cls")
                print("Caracter inválido, solo se permiten valores numéricos")
            else:      
                isActive=False
        isActive = True
        while isActive:
            try:
                peso = float(input("Ingrese el peso del alumno en kg: "))
                while peso <= 0:
                    print("El peso no puede ser negativo ni 0")
                    peso = float(input("Ingrese el peso del alumno en kg: "))
            except ValueError:
                os.system("cls")
                print("Caracter inválido, solo se permiten valores numéricos")
                
            else:
                isActive = False
        isActive = True
        while isActive:
            try:
                altura = float(input("Ingrese la altura del alumno en metros: "))
                while altura <= 0:
                    print("La altura no puede ser negativa ni 0")
                    altura = float(input("Ingrese la altura del alumno en metros: "))  
            except ValueError:
                os.system("cls")
                print("Caracter inválido, solo se permiten valores numéricos")
                
            else:
                isActive = False
            os.system("cls")
          
        estudiante = Alumnos(nombre, edad, peso, altura)
        """ print(f"Nombre: {estudiante.nombre}")
        print(f"Edad: {estudiante.edad}")
        print(f"IMC: {estudiante.imc()}")
        print(f"Rango: {estudiante.rango()}") """
        rango = estudiante.rango()
        
        if rango == "Normal":
            contadorImc[0] += 1
        elif rango == "Sobrepeso":  
            contadorImc[1] += 1
        elif rango == "Obesidad":
            contadorImc[2] += 1
        elif rango == "Obesidad 2":
            contadorImc[3] += 1
        elif rango == "Obesidad 3":
            contadorImc[4] += 1  
        os.system("pause")     
titulo="""
********************************
*        RESULTADOS IMC        *
********************************
"""
print(titulo)
print(" ╔═════════════════════════════════╦═══════════════════╗")       
print(f"║Estudiantes con peso ideal ----> ║{contadorImc[0]}   ║")
print(" ║=================================║===================║")
print(f"║Estudiantes con sobrepeso -----> ║{contadorImc[1]}   ║")
print(" ╠=================================║===================║")
print(f"║Estudiantes con obesidad ------> ║{contadorImc[2]}   ║")
print(" ║=================================║===================║")
print(f"║Estudiantes con obesidad 2-----> ║{contadorImc[3]}   ║")
print(" ║=================================║===================║")
print(f"║Estudiantes con obesidad 3-----> ║{contadorImc[4]}   ║")
print(" ╚═════════════════════════════════╩═══════════════════╝") 