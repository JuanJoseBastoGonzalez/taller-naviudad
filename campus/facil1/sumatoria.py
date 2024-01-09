numeros = [0,0,"primer","segundo","tercero"]
def entero():
        print("El numero tiene que ser entero")
        numeros[0] = int(input(f"Ingrese el {i} número: "))   
for i in numeros[2:5]:
  try:
    numeros[0] = int(input(f"Ingrese el {i} número: "))
  except ValueError:
    entero()
    while numeros[0] < 0:
     print("El número no puede ser negativo") 
    try:
      numeros[0] = int(input(f"Ingrese el {i} número: ")) 
    except ValueError:
      entero()
  if numeros[0] > 0:
    numeros[1] += numeros[0]
    print(numeros[1])  