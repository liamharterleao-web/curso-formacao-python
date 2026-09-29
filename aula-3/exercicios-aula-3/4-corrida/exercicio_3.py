print("Corrida — recibo")

km = float(input("Km: "))
preco_km = float(input("Preco por km: "))
bandeirada = float(input("Bandeirada: "))

preco_km_total =  km * preco_km
total =  bandeirada + preco_km_total

print("=" * 30)
print(f"Km:         {km}")
print(f"Preco/km:   R$ {preco_km:.2f}")
print(f"Bandeirada: R$ {bandeirada:.2f}")
print("-" * 30)
print(f"TOTAL:      R$ {total:.2f}")
print("=" * 30)

#Corrida — recibo
#Km: 8.2
#Preco por km: 2.40
#Bandeirada: 5.50
#==============================
#Km:         8.2
#Preco/km:   R$ 2.40
#Bandeirada: R$ 5.50
#------------------------------
#TOTAL:      R$ 25.18
#==============================
