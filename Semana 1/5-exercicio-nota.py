A, B = map(float, input().split())

MEDIA = (A + B) / 2

if MEDIA >= 7:
	print('Aprovado')
elif MEDIA >=4:
	print('Recuperacao')
else:
	print('Reprovado')