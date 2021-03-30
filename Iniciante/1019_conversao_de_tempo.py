duracao_seg = int(input())

h = duracao_seg // 3600
m = duracao_seg % 3600 // 60
s = duracao_seg % 60

print(f'{h}:{m}:{s}')
