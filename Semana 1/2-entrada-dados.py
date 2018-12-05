# input de inteiros
a = int(input())
b = int(input())

print(a + b)

# ou na mesma linha
a, b = input().split()

print(int(a) + int(b))

# Excercio com divisão e duas casas decimais

a = float(input())
b = float(input())

print("{:.2f}".format(a/b))