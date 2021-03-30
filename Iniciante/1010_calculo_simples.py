e1 = input()
e2 = input()

p1 = e1.split(' ')
cp1 = int(p1[0])
np1 = int(p1[1])
vup1 = float(p1[2])

p2 = e2.split(' ')
cp2 = int(p2[0])
np2 = int(p2[1])
vup2 = float(p2[2])

val_pagar = np1 * vup1 + np2 * vup2

print(f'VALOR A PAGAR: R$ {val_pagar:.2f}')
