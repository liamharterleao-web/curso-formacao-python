print("Fatura de energia")

titular = input("Titular: ")
kwh = int(input("kWh: "))
tarifa = float(input("Tarifa: "))
taxa = float(input("Taxa iluminacao: "))

consumo =  kwh * tarifa
total =  consumo + taxa

print()
print("=" * 34)
print("COMPANHIA PYTHON DE ENERGIA")
print("=" * 34)
print(f"Titular:  {titular}")
print(f"kWh:      {kwh}")
print(f"Tarifa:   R$ {tarifa:.2f}")
print(f"Consumo:  R$ {consumo:.2f}")
print(f"Taxa:     R$ {taxa:.2f}")
print("-" * 34)
print(f"TOTAL:    R$ {total:.2f}")
print("=" * 34)