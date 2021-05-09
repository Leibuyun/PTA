n, m = input().split()
n, m = int(n), int(m)
m %= n
lst = input().split()
lst = lst[::-1]
lst = lst[m - 1::-1] + lst[:m - 1:-1]
print(*lst)