from datetime import datetime
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

valor_total = float
nome_do_atendente = input("Nome do atendente?")
numero = 0
valor_unitario_check = ""
produtos = []
valor_final = 00.00

continuar = input("Deseja cadastrar um produto? (Sim/Não): ")

while continuar.lower() == "sim" or continuar.lower() == "s":
        numero += 1

        nome_do_produto = input("Qual o nome do produto?")
        valor_unitario = input("Qual o valor unitário desse produto?")
        quantidade = input("Quantas unidades desse produto é necessário?")

        if "," in valor_unitario:
          valor_unitario_check = valor_unitario.replace(",",".")
        else:
          valor_unitario_check = valor_unitario

        valor_total = float(valor_unitario_check) * int(quantidade)

        espacamento = ("=" * 20)
        produtos.append (
            {"item":  nome_do_produto,
             "qtd": quantidade,
             "valor_unidade": valor_unitario_check,
             "subtotal": valor_total
             })
        continuar = input("Deseja cadastrar mais um produto? (Sim/Não): ")

print("")
print(espacamento)
print("CUPOM FISCAL")
print(espacamento)
print("ATENDENTE: ", nome_do_atendente)
print("DATA E HORA: ", data_formatada)
print(espacamento)

while numero > 0:
  valor_final += produtos[numero-1]['subtotal']
  print("PRODUTO: ", produtos[numero-1]['item'], " QUANTIDADE: ", produtos[numero-1]['qtd'], " VALOR UNITÁRIO: ", produtos[numero-1]['valor_unidade'], " SUBTOTAL: ", produtos[numero-1]['subtotal'])
  numero -=1
  if numero == 0:
      print(espacamento)
      print("VALOR FINAL: R$ ", (f"{valor_final:.2f}"))
