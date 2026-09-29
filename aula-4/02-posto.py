
# Posto — comum ou aditivada
# Sem laço, sem lista, sem try.
#
# Regras:
# - comum: preco digitado
# - aditivada: preco + 0.40 por litro
# - outro tipo: recusar, sem total
# - litros <= 0: recusar, sem total
#
# Casos:
# 10 litros comum a 6.20 → R$ 62.00
# 10 litros aditivada a 6.20 → R$ 66.00
import sys

print("Posto")
tipo = input("Tipo (comum/aditivada): ")
if tipo not in ["comum", "aditivada"]:
    sys.exit()

litros = float(input("Litros: "))
preco = float(input("Preco do litro (comum): "))


if litros <= 0:
    sys.exit()

if tipo == "comum":
    total = preco * litros
    print(f"TOTAL: R$ {total:.2f}")
elif tipo == "aditivada":
    total = preco * litros + (litros * 0.40)
    print(f"TOTAL: R$ {total:.2f}")