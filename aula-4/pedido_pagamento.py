nome = input("Qual o nome do produto?")
quantidade = int(input("Qual a quantidade?"))

if quantidade < 1:
    print("Quantidade inválida")
else:

    preco = float(input("Qual o valor unitário?"))
    forma = input("Escreva o meio de pagamento: dinheiro, cartão ou pix")

    subtotal = quantidade * preco

    if forma not in ["dinheiro", "cartão", "cartao", "pix"]:    
        print(f"A forma de pagamento {forma} não é aceita")
    else:
        dinheiro = subtotal - 0.9
        cartao = subtotal + 0.5
        pix = subtotal

        #INICIO DO RECIBO
        print()
        print("=" * 32)
        print("LANCHONETE SABOR E CODIGO")
        print("=" * 32)
        print(f"Item:     {nome}")
        print(f"Qtd:      {quantidade}")
        print(f"Unitário: {preco:.2f}")
        print(f"Forma   : {forma}")
        print(f"SUBTOTAL:    {subtotal:.2f}")
        print

        #MEIO DO RECIBO
        if forma == "dinheiro":
            print(f"TOTAL: R$ {dinheiro:.2f} no dinheiro")
        elif forma == "cartão" or forma == "cartao":
            print(f"TOTAL: R$ {cartao:.2f} no cartão")
        elif forma == "pix":
                print(f"TOTAL: R$ {pix:.2f} no pix")

        #FINAL DO RECIBO
        print()
        print("-" * 32)
        print()
        print("=" * 32)