lst = input().split()
a, da, b, db = int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3])
p1 = 0
while a != 0:
    if a % 10 == da:
        p1 = p1 * 10 + da
    a //= 10
p2 = 0
while b != 0:
    if b % 10 == db:
        p2 = p2 * 10 + db
    b //= 10
print(p1 + p2)