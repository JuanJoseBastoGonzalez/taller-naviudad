xn =7
for f in range(1,8):
    serie=""
    if f >= 5:
        xn +=2
    for c in range(1,xn-f):
        serie = serie + str("*")
    print(serie)