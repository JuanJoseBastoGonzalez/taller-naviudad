import os            
numeros = []
total_numeros = 0
total_pares = 0
total_impares = 0
suma_pares = 0
suma_impares = 0
menores_que_10 = 0
entre_20_y_50 = 0
mayores_que_100 = 0

while True:
    os.system("cls")
    titulo="""
    ********************************
    *      CONTADOR DE NUMEROS     *
    ********************************
    """
    print(titulo)
    try:
        num = int(input("Ingrese un número entero positivo (ingrese un número negativo para terminar): "))
        if num >= 0:
            numeros.append(num)
            total_numeros += 1

            if num % 2 == 0:
                total_pares += 1
                suma_pares += num
            else:
                total_impares += 1
                suma_impares += num

            if num < 10:
                menores_que_10 += 1
            elif 20 <= num <= 50:
                entre_20_y_50 += 1
            elif num > 100:
                mayores_que_100 += 1
        else:
            break
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if total_pares > 0:
    promedio_pares = suma_pares / total_pares
else:
    promedio_pares = 0

if total_impares > 0:
    promedio_impares = suma_impares / total_impares
else:
    promedio_impares = 0



titulo= """
****************************
*        RESULTADOS        *
****************************
"""
print(titulo)
print(f"╔══════════════════════════════════════════════════════════╗")
print(f"║                         REPORTES                         ║")
print(f"╠═══════════════════════════════════════╦══════════════════╣ ")
print(f"║a. Total de números ingresados         ║{total_numeros}     ║")
print(f"║b. Total de números pares ingresados   ║{total_pares}     ║")
print(f"║c. Promedio de los números pares       ║{promedio_pares}     ║")
print(f"║d. Promedio de los números impares     ║{promedio_impares}      ║")
print(f"║e. Cuantos números son menores que 10  ║{menores_que_10}     ║")
print(f"║f. Cuantos números están entre 20 y 50 ║{entre_20_y_50}       ║")
print(f"║g. Cuantos números son mayores que 100 ║{mayores_que_100}      ║")
print(f"╚═══════════════════════════════════════╩══════════════════╝")
