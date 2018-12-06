dias = int(input())
lista = []
total = 0
final = -1
for i in range(0, dias):
    lista.append(int(input()))

for i in range(0, len(lista)):
    total += lista[i]
    if total >= 1000000 and final == -1:
        final = i + 1
print(final)