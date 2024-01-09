""" 4. Se desea realizar un programa en Python que permita ingresar n números enteros positivos y cuando se
Ingrese un numero negativo debe mostrar en pantalla el siguiente reporte.

a. Total de números ingresados
b. Total de números pares ingresados
c. Promedio de los números pares
d. Promedio de los números impares
e. Cuantos números son menores que 10
f. Cuantos números están entre 20 y 50
g. Cuantos números son mayores que 100 """
numeros=[]
listaN =[]
x=1

while x > 0:
    for i in range(0,x):
        try:
            numeros= int(input("ingrese un numero"))
        except ValueError:
             print("solo se permiten valores enteros")
             numeros= int(input("ingrese un numero"))
      
        totalN = len(numeros())
        NumPares = sum(1 for num in numeros if num % 2 == 0)
        NumImpares = totalN - NumPares
        proPares = sum(num for num in numeros if num % 2 == 0) / NumPares if NumPares > 0 else 0
        PromedioImp = sum(num for num in numeros if num % 2 != 0) / NumImpares if NumImpares > 0 else 0
        menores_que_10 = sum(1 for num in numeros if num < 10)
        entre_20_y_50 = sum(1 for num in numeros if 20 <= num <= 50)
        mayores_que_100 = sum(1 for num in numeros if num > 100)
        
        listaN.append(numeros)
        print(listaN)
        if numeros <= 0:
            print(totalN)
            print(NumPares)
            print(NumImpares)
            print(PromedioImp)
            print(menores_que_10)
            print(entre_20_y_50)
            print(mayores_que_100)





            x = -1   
        print("hola")
            