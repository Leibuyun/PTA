lst = input().split()
length = len(lst)
a, b = int(lst[0]) * int(lst[1]), int(lst[1]) - 1
if b + 1:
    print(a, b, end='')
else:
    print(0, 0)
for i in range(2, length - 1, 2):
    a, b = int(lst[i]) * int(lst[i + 1]), int(lst[i + 1]) - 1
    if b + 1:
        print('', a, b, end='')
