questoes = int(input())

respostas_corretas = input()
respostas_respondidas = input()

final = 0

for i in range(len(respostas_corretas)):
    if respostas_corretas[i] == respostas_respondidas[i]:
        final = final + 1

print (final)
