# Loja VIP — desconto com minimo
# Sem laço, sem lista, sem try.
#
# Regras:
# - total <= 0: recusar
# - vip == "s"  e  total >= 100: 15% de desconto
# - vip certo mas total baixo: mensagem "minimo nao atingido", preco cheio
# - nao VIP: preco cheio, mensagem "sem desconto VIP"4
#
# Fronteira: VIP e 100.00 → desconto. VIP e 99.99 → sem desconto.
import sys

print("Loja VIP")
vip = input("Cliente VIP (s/n): ")
total = float(input("Total da compra: "))

# complete: and, mensagens distintas, R$ com :.2f
if total <= 0:
    sys.exit("Valor total inválido")
if vip == "s" and total >= 100:
    total *= 0.85
    print(f"Valor mínimo para desconto atingido. TOTAL = R$ {total:.2f}")
elif vip == "s" and total < 100:
    print(f"Valor mínimo para desconto não atingido. TOTAL = R$ {total:.2f}")
if vip not in "s":
    print(f"Valor sem desconto VIP = R$ {total:.2f}")