val_monetario = float(input()) + 0.0001

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

qtd = 0
resto = 0
if 0 < val_monetario < 1000000.00:
    print('NOTAS:')
    for n in notas:
        if qtd == 0 and resto == 0:
            qtd = val_monetario // n
            resto = val_monetario % n
        else:
            qtd = resto // n
            resto = resto % n
        print(f'{qtd:.0f} nota(s) de R$ {n:.2f}')

    print('MOEDAS:')
    for m in moedas:
        qtd = resto // m
        resto = resto % m
        print(f'{qtd:.0f} moeda(s) de R$ {m:.2f}')
