# Aula 6 — Estruturas de repetição

Uma estrutura de repetição executa o mesmo bloco várias vezes. Nesta aula entram `for`, `range`, `while`, `break`, `continue` e `pass`.

---

## `for` e `range`

O `for` repete o bloco uma vez para cada valor. O `range` produz a sequência de inteiros que o `for` percorre.

`range(4)` produz `0`, `1`, `2`, `3`. A contagem começa em 0 e para antes do 4. São quatro voltas.

`range(1, 4)` produz `1`, `2`, `3`. A contagem começa no primeiro número e para antes do segundo.

`range(1, n + 1)` leva a contagem de 1 até `n`. Com `n = 3`, a sequência é `1`, `2`, `3`.

```python
print("range(4)")
for i in range(4):
    print(i)

print("range(1, 4)")
for i in range(1, 4):
    print(i)

n = 3
print("range(1, n + 1)")
for i in range(1, n + 1):
    print(i)
```

Saída:

```text
range(4)
0
1
2
3
range(1, 4)
1
2
3
range(1, n + 1)
1
2
3
```

Em cada volta, `i` recebe o próximo número e o `print` mostra esse número.

---

## Acumulador

O acumulador é uma variável criada antes do `for`. Ela guarda a soma de todas as voltas. Dentro do laço, cada volta só acrescenta o valor da vez.

```python
total = 0
for i in range(1, 4):
    total = total + i
    print("volta", i, "total", total)
print("resultado", total)
```

Saída:

```text
volta 1 total 1
volta 2 total 3
volta 3 total 6
resultado 6
```

`total` começa em 0. A volta 1 soma 1 (fica 1). A volta 2 soma 2 (fica 3). A volta 3 soma 3 (fica 6). O `print` do resultado fica fora do `for` e aparece uma vez só.

---

## `while`

O `while` repete o bloco enquanto a condição for verdadeira. Dentro do bloco, alguma linha precisa alterar essa condição. Quando `n` passa de 3, `n <= 3` fica falsa e a repetição acaba.

```python
n = 1
while n <= 3:
    print(n)
    n = n + 1
print("terminou", n)
```

Saída:

```text
1
2
3
terminou 4
```

A linha `print("terminou", n)` está fora do `while`. Ela roda depois que a condição deixa de valer.

---

## `break`

O `break` encerra o laço naquela volta. A execução segue na primeira linha depois do laço.

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
print("saiu")
```

Saída:

```text
1
2
3
saiu
```

Nas voltas 1, 2 e 3 o `if` não dispara e o número é impresso. Na volta 4 o `break` sai do `for`. O 5 não chega a existir nessa execução. `saiu` está fora do laço.

`while True` repete sem uma condição de parada no `while`. O `break` é o que encerra.

```python
while True:
    texto = input("Digite um numero ou sair: ")
    if texto == "sair":
        break
    print("recebi", texto)
print("fim")
```

Cada texto diferente de `sair` é impresso e a pergunta volta. `sair` dispara o `break`. `fim` está fora do laço e aparece em seguida.

---

## `continue`

O `continue` pula o resto da volta atual e começa a volta seguinte. O laço não acaba. O que já foi somado permanece.

```python
total = 0
for i in range(1, 6):
    if i == 3:
        continue
    total = total + i
    print("somou", i, "total", total)
print("resultado", total)
```

Saída:

```text
somou 1 total 1
somou 2 total 3
somou 4 total 7
somou 5 total 12
resultado 12
```

Quando `i` vale 3, o `continue` não executa a soma nem o `print` daquela volta. As voltas 1, 2, 4 e 5 somam. O resultado é `1 + 2 + 4 + 5 = 12`.

---

## `pass`

O `pass` é uma instrução vazia. Ele ocupa um bloco que o Python exige e a execução segue na linha de baixo.

```python
opcao = "b"
if opcao == "b":
    pass
    print("opcao b ainda sem acao")
print("seguiu")
```

Saída:

```text
opcao b ainda sem acao
seguiu
```

O `if` tem um corpo válido por causa do `pass`. O `print` seguinte roda na mesma volta. `seguiu` está fora do `if`.
