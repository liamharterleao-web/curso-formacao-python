# Meia-entrada — estudante e idade
# Sem laço, sem lista, sem try.
#
# Regras:
# - idade < 1: recusar
# - estudante == "s"  e  idade < 18: meia (preco * 0.5)
# - caso contrario: inteira (preco cheio) com mensagem "sem meia"
#
# Fronteira: estudante "s" e idade 17 → meia. Idade 18 → inteira.

print("Meia-entrada")
idade = int(input("Idade: "))
estudante = input("Estudante (s/n): ")
preco = float(input("Preco do ingresso: "))

# complete: and, print do valor ou recusa
