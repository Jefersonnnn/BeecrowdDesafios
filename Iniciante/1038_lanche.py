cod, qtd = list(map(int, input().split(' ')))
precos = [4, 4.5, 5, 2, 1.5]
tot = precos[cod - 1] * qtd
print(f'Total: R$ {tot:.2f}')
