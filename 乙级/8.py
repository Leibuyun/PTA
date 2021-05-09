n, m = input().split()
n, m = int(n), int(m)
m %= n
lst = input().split()
lst = lst[::-1]  # 整体翻转
lst = lst[m - 1::-1] + lst[:m - 1:-1]  # 前m个和后n-m个都翻转, 之后合并
print(*lst)
