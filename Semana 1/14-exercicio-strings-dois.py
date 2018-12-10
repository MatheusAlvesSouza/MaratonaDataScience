S = input()

vogais = ['a', 'e', 'i', 'o', 'u']

R = ''

for c in S:
    if c in vogais:
        R += c

# R[::1] string ao inverso instrução chamada slice
if R == R[::-1]:
    print('S')
else:
    print('N')
