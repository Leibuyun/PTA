t = int(input())
for i in range(1, t + 1):
    lst = input().split()
    print(f'Case #{i}:', 'true' if int(lst[0]) + int(lst[1]) > int(lst[2]) else 'false')
