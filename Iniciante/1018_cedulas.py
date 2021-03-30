valor = int(input())
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

qtd = 0
resto = 0
if 0 < valor < 1000000:
    print(valor)
    for n in notas:
        if qtd == 0 and resto == 0:
            qtd = valor // n
            resto = valor % n
        else:
            qtd = resto // n
            resto = resto % n
        n = f'{n:.2f}'.replace('.', ',')
        print(f'{qtd:.0f} nota(s) de R$ {n}')
