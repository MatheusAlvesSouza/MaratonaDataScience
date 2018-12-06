a, b, c = map(int, input().split())

if a != b and a !=c:
	resultado = 'A'
elif b != a and b != c:
	resultado = 'B'
elif c != b and c != a:
	resultado = 'C'
else:
	resultado = '*'

print(resultado)