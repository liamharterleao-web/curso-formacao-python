"""
Realizar tarefa até segunda-feira (04 de outubro)

Listas
Dicionário
Tupla
Funções

while True:

    nome = input("Qual seu nome? ")
    if nome == "Eduardo":
        print("olá Eduardo")
        idade = int(input("Qual sua idade? "))
    else:
        break

    if idade > 18:
        print("Olá adulto!")
        break
"""
f_numero = None
s_numero = None
while True:
    numero = int(input("Digite o primeiro número do array entre 1 e 5"))
    if f_numero in range(1,5):
        print("Opção inválida")
        continue
    else:
        s_numero = int(input("Digite o numero final do array"))
        break
     
print(f"Número {range(f_numero, s_numero)} é valido")
