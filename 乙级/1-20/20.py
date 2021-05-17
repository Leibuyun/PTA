class A:
    def __init__(self, s, p):
        self.s = s
        self.p = p


n, d = map(lambda x: int(x), input().split())
lst1 = input().split()
lst2 = input().split()
arr = []
for i in range(n):
    # 必须是float， 题目说的是正数， 没说正整数， 醉了
    arr.append(A(float(lst1[i]), float(lst2[i])))
arr.sort(key=lambda x: x.p/x.s, reverse=True)
ans = i = 0
while i < n:
    if d >= arr[i].s:
        ans += arr[i].p
        d -= arr[i].s
    else:
        ans += d * arr[i].p / arr[i].s
        break
    i += 1
print(f'{ans:.2f}')
