total = float(0)
desc = 0
for cont in range(1,11):
    consumo = input("ingrese un numero")
    total += float(consumo)
if total >50:
    desc = total*0.07
print(f"consumo total {total}")
print(f"descuento {desc}")
print(f"pago total {total-desc}")