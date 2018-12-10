n = int(input())
lista = map(int, input().split())

#lista.sort() # ASC
#lista.sort(reverse = True) # DESC

for l in sorted(lista):
    print(l, end=' ')