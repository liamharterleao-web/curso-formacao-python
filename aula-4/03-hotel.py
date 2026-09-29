# Hotel — alta ou baixa temporada
# Sem laço, sem lista, sem try.
#
# Regras:
# - alta: diaria * 1.20
# - baixa: diaria cheia
# - outra temporada: recusar, sem total
# - diarias < 1: recusar, sem total
#
# Casos:
# 3 diarias baixa a 180.00 → R$ 540.00
# 3 diarias alta a 180.00 → R$ 648.00

import sys

print("Hotel")
temporada = input("Temporada (alta/baixa): ")
diarias = int(input("Diarias: "))
valor = float(input("Valor da diaria: "))

alta = diarias * valor * 1.20
baixa = diarias * valor

if diarias < 1:
    sys.exit()

if temporada == "alta":
    print(f"TOTAL: R$ {alta:.2f}")
if temporada == "baixa":
    print(f"TOTAL: R$ {baixa:.2f}")