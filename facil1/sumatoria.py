import os
numeros = [0,0,"primer","segundo","tercero"]
def entero():
        
        # numeros[0] = int(input(f"Ingrese el {i} número: "))   
  for i in numeros[2:5]:
    isActive=True
    while isActive:
      os.system("cls")
      
      try:
        numeros[0] = int(input(f"Ingrese el {i} número: "))
        while numeros[0] < 0:
          print("El número no puede ser negativo") 
          numeros[0] = int(input(f"Ingrese el {i} número: ")) 
      except ValueError:
        print("Tine que ser un numero entero")
        os.system("pause")
        
      else:
        isActive= False
        
      # try:
      #   numeros[0] = int(input(f"Ingrese el {i} número: ")) 
      # except ValueError:
      #   print("El numero tiene que ser entero")
    if numeros[0] > 0:
        numeros[1] += numeros[0]
        print(numeros[1])  
entero()