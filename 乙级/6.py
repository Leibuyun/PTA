num = int(input())
b = num // 100
print('B' * b, end='')
s = num // 10 % 10
print('S' * s, end='')
g = num % 10
for i in range(1, g + 1):
    print(i, end='')
