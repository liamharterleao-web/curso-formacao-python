# Cinema — inteira ou meia
# Sem laço, sem lista, sem try.
#
# Regras:
# - inteira: preco cheio
# - meia: metade do preco
# - outro tipo: recusar, sem total
# - quantidade < 1: recusar, sem total
#
# Casos:
# 3 inteira a 28.00 → R$ 84.00
# 2 meia a 28.00 → R$ 28.00
# 0 inteira → recusa
import sys

print("Bilheteria")
tipo = input("Tipo (inteira/meia): ")

if tipo not in ["inteira", "meia"]:
    print(f"Tipo de pagamento '{tipo}' é inválido")    
    sys.exit()

quantidade = int(input("Quantidade: "))

if quantidade < 0:
    sys.exit()

preco = float(input("Preco do ingresso: "))
subtotal = quantidade * preco

total = None #Preciso declarar a variável antes de somar ela por ela mesma (total += subtotal)

if tipo == "inteira":
    total += subtotal
elif tipo == "meia":
    total = subtotal/2
print(f"Valor total R$ {total:.2f}")

# total = total / 2
# Tem o mesmo resultado que:
# total /= 2