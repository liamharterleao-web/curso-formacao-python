# Meia-entrada — estudante e idade
# Sem laço, sem lista, sem try.
#
# Regras:
# - idade < 1: recusar
# - estudante == "s"  e  idade < 18: meia (preco * 0.5)
# - caso contrario: inteira (preco cheio) com mensagem "sem meia"
#
# Fronteira: estudante "s" e idade 17 → meia. Idade 18 → inteira.

import sys

print("Meia-entrada")
idade = int(input("Idade: "))
estudante = input("Estudante (s/n): ")
preco = float(input("Preco do ingresso: "))

if idade < 1:
    sys.exit("Não é permitida a entrada de crianças abaixo de um ano")
total = None

if idade < 18 and estudante == "s":
    total = preco * 0.5  
    print(f"TOTAL R$ {total}, valor com meia entrada")
elif idade < 18 and estudante not in "s":
    total = preco
    print(f"TOTAL R$ {total}, valor sem meia entrada")  
if idade > 17:
    total = preco
    print(f"TOTAL R$ {total}, valor sem meia entrada")