# Aula 5 — Várias regras \+ `match` na forma

O pagamento da Aula 4 já escolhe um caminho com `if`/`elif`. Hoje duas novidades:

1. **Duas perguntas verdadeiras ao mesmo tempo** (`and` / `or` / `not`): cupom só vale com subtotal alto; embalagem só em viagem com pedido baixo.  
2. **Outro jeito de escolher a forma** — `match` / `case` (o *switch* de outras linguagens).

Ainda é **um** item. Vários itens são a Aula 6\.

---

## `and`, `or`, `not`

| Palavra | Significado |
| :---- | :---- |
| `and` | as **duas** condições verdadeiras |
| `or` | **pelo menos uma** verdadeira |
| `not` | inverte (tem cupom? não tem?) |

cupom certo  e  subtotal \>= 25  →  aplica 10%

viagem  e  subtotal \< 15        →  \+ R\$ 2,00 de embalagem

Se só uma for verdadeira, a regra **não** aplica. 24.99 não é 25\.

---

## Tabela verdade

Cada condição é **V** (verdadeira) ou **F** (falsa). A tabela lista **todas** as combinações — assim você prevê o resultado **antes** de rodar.

### `and` — só V se as duas forem V

| A | B | A `and` B |
| :---- | :---- | :---- |
| V | V | **V** |
| V | F | F |
| F | V | F |
| F | F | F |

Cupom: A \= “código certo”, B \= “subtotal ≥ 25”. Só a primeira linha aplica o desconto.

### `or` — V se pelo menos uma for V

| A | B | A `or` B |
| :---- | :---- | :---- |
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | F |

Login inválido: A \= “senha vazia”, B \= “tamanho \< 4”. Qualquer V → recusa.

### `not` — inverte

| A | `not` A |
| :---- | :---- |
| V | F |
| F | **V** |

Cupom vazio é F em “tem cupom?” → `not cupom` é V → caminho “sem cupom”.

No papel, marque a linha da tabela **antes** de apertar ▶.

---

## Ordem das regras

1. Quantidade \< 1 → recusar e **parar**.  
2. Calcular o subtotal.  
3. Cupom (código **e** mínimo).  
4. Viagem e embalagem (sobre o valor **já** com cupom, se houver).  
5. Forma de pagamento (`match`).  
6. Ticket.

O cliente precisa de uma **mensagem** quando o cupom não entra.

---

## Fronteira

- Subtotal `25.00` \+ `LANCHE10` → desconto aplica.  
- Subtotal `24.00` \+ `LANCHE10` → desconto **não** aplica; aviso claro.

`>=` inclui o 25\. `>` deixaria o 25 de fora.

---

## `not` no cupom vazio

se não tem cupom → "sem cupom"

Não é erro. É um caminho.

---

## `match` / `case` (o “switch” do Python)

Quando **um** valor escolhe entre opções com nome, o Python 3.10+ tem `match` / `case`. Em outras linguagens isso costuma se chamar *switch*.

A forma da Aula 4 (`dinheiro` / `cartao` / `pix`) é o caso clássico:

match forma:

    case "dinheiro":

        total \= valor \* 0.9

    case "cartao":

        total \= valor \* 1.05

    case "pix":

        total \= valor

    case \_:

        print("Forma desconhecida.")

        total \= None

`case _` \= “qualquer outra coisa” (ex.: `boleto`). Não use o `case` do PIX como “resto”.

| Situação | Preferir |
| :---- | :---- |
| Faixa / comparação (`quantidade < 1`) | `if` |
| Duas condições ao mesmo tempo (cupom) | `and` / `or` |
| Um valor entre opções nomeadas (forma) | `match` (ou `elif`) |

`match` **não** substitui `and` no cupom.

---

## O que fazer hoje

Arquivo: `validador_pedido.py` na pasta `aula-05`.

1. Ler item, quantidade, preço.  
2. Recusar quantidade inválida.  
3. Ler cupom (pode ser vazio) e viagem (`s`/`n`).  
4. Aplicar cupom e embalagem com `and` / `or` / `not`.  
5. Ler a forma e aplicar com `match` / `case`.  
6. Ticket com `R$` e `:.2f`.

---

## Casos para conferir

Ordem: subtotal → cupom → embalagem → forma.

| Caso | Qtd | Preço | Cupom | Viagem | Forma | Conferir |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 2 | 8.50 | (vazio) | `n` | `pix` | 17.00 |
| 2 | 4 | 8.50 | `LANCHE10` | `n` | `pix` | 34 → 10% → `30.60` |
| 3 | 4 | 8.50 | `LANCHE10` | `s` | `pix` | `30.60`; sem embalagem |
| 4 | 1 | 8.50 | (vazio) | `s` | `pix` | `10.50` (8.50 \+ 2\) |
| 5 | 3 | 8.00 | `LANCHE10` | `n` | `pix` | 24.00; cupom **não** |
| 6 | 2 | 8.50 | (vazio) | `n` | `dinheiro` | `15.30` (`match`) |
| 7 | 0 | 8.50 | — | — | — | recusa |

Mínimo: casos **2**, **4**, **5** e **6**.

---

## Como saber se funcionou

- Um caso em que o cupom **não** aplica tem mensagem.  
- Um caso em que a embalagem **aplica** soma R\$ 2,00.  
- Você aponta o `case` da forma no código.

Depois do validador, há **10** exercícios curtos (frete → ingresso). Na aula: priorize **1–4**; o restante é para quem terminar cedo ou para recuperação.