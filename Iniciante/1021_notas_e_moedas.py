"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""

val_monetario = float(input()) + 0.0001

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

qtd = 0
resto = 0
if 0 < val_monetario < 1_000_000.00:
    print('NOTAS:')
    for nota in notas:
        if qtd == 0 and resto == 0:
            qtd = val_monetario // nota
            resto = val_monetario % nota
        else:
            qtd = resto // nota
            resto = resto % nota
        print(f'{qtd:.0f} nota(s) de R$ {nota:.2f}')

    print('MOEDAS:')
    for moeda in moedas:
        qtd = resto // moeda
        resto = resto % moeda
        print(f'{qtd:.0f} moeda(s) de R$ {moeda:.2f}')
