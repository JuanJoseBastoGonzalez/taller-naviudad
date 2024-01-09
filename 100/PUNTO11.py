pro=int(1)
n = int(input("valor de n"))
for f in range(1,n+1):
    print(f"{f} ")
    pro *= f 
    print(f"\n producto de  {n} es {pro}")