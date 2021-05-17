n = int(input())
cnt = 0
while n != 1:
    cnt += 1
    n = n // 2 if n & 1 == 0 else (3 * n + 1) // 2
print(cnt)
