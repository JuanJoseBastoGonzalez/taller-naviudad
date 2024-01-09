a = int(input("numero a"))
b = int(input("numero b"))
if a <b:
    for n in range(a+1,b-1):
        print(n)
else:
    for n in range(b+1,a-1):
        print(n)
        