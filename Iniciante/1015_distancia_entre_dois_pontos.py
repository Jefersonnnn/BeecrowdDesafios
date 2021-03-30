from math import sqrt

x1, y1 = list(map(float, input().split(' ')))
x2, y2 = list(map(float, input().split(' ')))

dist = sqrt((x2 - x1)**2 + (y2 - y1) **2)

print(f'{dist:.4f}')
