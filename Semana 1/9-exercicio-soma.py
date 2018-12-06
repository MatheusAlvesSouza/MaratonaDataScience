fim = int(input())

if 1 <= fim and fim <= 100:
    lista = map(int, input().split())

print(sum(lista))