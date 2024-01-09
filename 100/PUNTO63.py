costo, iva, TotPagar = 0.0, 0.0, 0.0
print("Costo de la Casa S/.")
costo = float(input())
print("Valor del IVA (%):")
iva = float(input())
TotPagar = costo + (costo * (iva / 100))
print(f"IVA {iva}% S/. {(costo * (iva / 100))}")
print(f"TOTAL A PAGAR S/. {TotPagar}")
