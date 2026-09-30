# Ingresso — tipo com match + idade
# Sem laço, sem lista, sem try. Python >= 3.10.
#
# Regras:
# - idade < 1: recusar
# - pista: R$ 80.00  (idade >= 16)
# - camarote: R$ 200.00 (idade >= 18)
# - meia: R$ 40.00 (idade >= 16  e  estudante == "s")
# - tipo desconhecido: recusar (case _)
# - idade insuficiente para o tipo: mensagem, sem total
#
# Use match no tipo. Use and na meia e nas idades minimas.
#
# Casos:
# pista, 16, n → 80.00
# camarote, 17, n → recusa idade
# meia, 16, s → 40.00
# meia, 16, n → sem meia / recusa
# vip → tipo desconhecido

print("Ingresso show")
tipo = input("Tipo (pista/camarote/meia): ")
idade = int(input("Idade: "))
estudante = input("Estudante (s/n): ")

# complete: match + and

if idade < 1:
    print("Recusado")

match tipo:
    case "pista" if idade >= 16:
        print("Total: R$ 80.00 - PISTA")
    case "meia" if idade >= 16 and estudante in ["s", "n"]:
        if estudante == "s":
            print("Total: R$ 40.00 - MEIA")
        else:
            print("Sem meia / recusado")
    case "camarote":
        if idade >= 18:
            print("Total: R$ 200.00 - CAMAROTE")
        else:
            print("Idade recusada para camarote")

if tipo not in ["pista", "camarote", "meia"]:
    print("Tipo desconhecido")