# Frete — peso e destino
# Sem laço, sem lista, sem try.
#
# Regras:
# - peso <= 0: recusar
# - capital  e  peso <= 5: frete R$ 12.00
# - interior e  peso <= 5: frete R$ 20.00
# - qualquer destino e peso > 5: frete R$ 35.00
#
# Fronteira: peso 5.00 em capital → 12.00 (nao 35.00)

import sys


print("Frete")
destino = input("Destino (capital/interior): ")

peso = float(input("Peso (kg): "))

if peso <= 0:
    sys.exit("Peso inválido.")

if peso <= 5:
    if  destino == "capital":
        print("Frete: R$ 12.00")
    elif destino == "interior":
        print("Frete: R$ 20.00")
else:
    if destino in ["capital", "interior"]:
        print("Frete: R$ 35.00")

