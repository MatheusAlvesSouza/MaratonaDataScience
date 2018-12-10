from math import sqrt

inputs = int(input())

raizes = map(float, input().split())

for i in raizes:
    print('{:.4f}'.format(sqrt(i)))
