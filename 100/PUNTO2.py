par = 0 
impar=0
for cont in range(1,11):
    num=int(input("ingrse un numero"))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    print(f"la cantidad de pares es {par}")
    print(f"la cantidad de impares  {impar}")