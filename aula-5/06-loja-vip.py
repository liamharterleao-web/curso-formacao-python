# Loja VIP — desconto com minimo
# Sem laço, sem lista, sem try.
#
# Regras:
# - total <= 0: recusar
# - vip == "s"  e  total >= 100: 15% de desconto
# - vip certo mas total baixo: mensagem "minimo nao atingido", preco cheio
# - nao VIP: preco cheio, mensagem "sem desconto VIP"
#
# Fronteira: VIP e 100.00 → desconto. VIP e 99.99 → sem desconto.

print("Loja VIP")
vip = input("Cliente VIP (s/n): ")
total = float(input("Total da compra: "))

# complete: and, mensagens distintas, R$ com :.2f
