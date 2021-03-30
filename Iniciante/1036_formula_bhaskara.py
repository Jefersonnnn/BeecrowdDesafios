A, B, C = list(map(float, input().split(' ')))

if A == 0 or (B**2 - 4 * A * C) < 0:
    print('Impossivel calcular')
else:
    R1 = (-B + (B**2 - 4 * A * C)**0.5) / (2 * A)
    R2 = (-B - (B**2 - 4 * A * C)**0.5) / (2 * A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
