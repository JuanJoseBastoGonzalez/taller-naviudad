alt = int(input('Altura del Triangulo: '))
caract = input('Ingrese un Caracter: ')
for i in range(1, alt + 1):
    for j in range(1, alt - i + 1):
        print(' ', end='')
    for j in range(1, (i * 2)):
        print(caract, end='')
    print()
