repeticoes = int(input())
opcoes = map(int, input().split())

lampada_um = 1
lampada_dois = 1

for i in opcoes:
    if(i == 1):
        lampada_um += 1
    if( i == 2):
        lampada_um += 1
        lampada_dois += 1

if lampada_um % 2 == 0:
    lampada_um = 1
else:
    lampada_um = 0

if lampada_dois % 2 == 0:
    lampada_dois = 1
else:
    lampada_dois = 0

print(lampada_um)
print(lampada_dois)