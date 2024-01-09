
P, A, B, Bb, h, L1, L2, L3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
print("ÁREA DEL TRAPECIO")
B = float(input("BASE MAYOR: "))
Bb = float(input("BASE MENOR: "))
h = float(input("ALTURA: "))
A = ((B + Bb) * h) / 2
print("ÁREA:", A)
print("\nPERÍMETRO DEL TRAPECIO")
L1 = float(input("LADO 01: "))
L2 = float(input("LADO 02: "))
L3 = float(input("LADO 03: "))
P = B + Bb + L1 + L2 + L3
print("PERÍMETRO:", P)
