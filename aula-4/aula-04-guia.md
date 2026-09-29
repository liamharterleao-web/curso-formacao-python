# Aula 4 — Um item, três formas de pagamento

O caixa da Aula 3 fecha 2 coxinhas a R\$ 8,50 em **R\$ 17,00** — sempre. Hoje o programa **escolhe um caminho**: dinheiro, cartão ou PIX mudam o total. Quantidade menor que 1 não entra.

Ainda é **um** item. Cupom, viagem e vários itens ficam para as próximas aulas.

---

## O que o `if` faz

Até agora o programa ia em linha reta: lê → calcula → imprime.

`if` pergunta. Se a resposta for verdadeira, entra num bloco. Se não for, tenta o próximo caminho (`elif`) ou o caminho restante (`else`).

se a forma for dinheiro → desconto

senão, se for cartao   → acréscimo

senão, se for pix      → preço cheio

senão                  → recusar

A **conta** continua sendo conta (`quantidade * preco`). O `if` só escolhe **qual** conta usar.

---

## `=` e `==`

| Símbolo | Significado |
| :---- | :---- |
| `=` | **guarda** um valor na variável |
| `==` | **pergunta** se dois valores são iguais |

`if forma = "pix"` quebra (`SyntaxError`). A pergunta usa `==`.

---

## Relacionais

| Operador | Pergunta |
| :---- | :---- |
| `==` | é igual? |
| `!=` | é diferente? |
| `>` `<` | maior / menor? |
| `>=` `<=` | maior ou igual / menor ou igual? |

Quantidade inválida: `if quantidade < 1:` → mensagem e **não** inventa total.

---

## Indentação

As linhas **mais para dentro** só rodam se a condição for verdadeira. Quatro espaços. Sem isso o Python reclama ou o bloco fica no lugar errado.

---

## Mesa de 3 linhas

Antes de apertar ▶, no papel:

1. **Entrada** — item, qtd, preço, forma  
2. **Condição** — qual `if` é verdadeiro?  
3. **Total** — o número que deve aparecer

---

## O que fazer hoje

Arquivo novo: `pedido_pagamento.py` na pasta `aula-04`.

1. Ler nome, quantidade, preço e forma (`dinheiro`, `cartao`, `pix`).  
2. Se quantidade \< 1: recusar e encerrar.  
3. Calcular o subtotal.  
4. Aplicar a forma de pagamento.  
5. Imprimir o ticket com `R$` e `:.2f`.

Forma desconhecida (`boleto`): recusar, não tratar como PIX.

---

## Casos para conferir

Subtotal \= quantidade × preço. Depois a forma altera o total.

| Caso | Item | Qtd | Preço | Forma | Total |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Coxinha | 2 | 8.50 | `dinheiro` | `R$ 15.30` |
| 2 | Coxinha | 2 | 8.50 | `cartao` | `R$ 17.85` |
| 3 | Coxinha | 2 | 8.50 | `pix` | `R$ 17.00` |
| 4 | Água | 0 | 3.00 | — | recusa; sem total |

Use ponto no decimal (`8.50`). Compare a forma em **minúsculas**.

---

## Como saber se funcionou

- Os casos 1 e 2 batem.  
- Quantidade 0 não imprime `R$`.  
- Você aponta, no código, a linha que escolhe o caminho.

O caderno Colab treina o conceito. O arquivo que vale é o `.py` no VS Code.

Quando o `pedido_pagamento.py` fechar, há três exercícios curtos em outros contextos (cinema, posto, hotel) — o mesmo `if`/`elif`/`else`.