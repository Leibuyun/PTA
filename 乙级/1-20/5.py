k = int(input())
nums = input().split()
nums.sort(key=lambda x: int(x), reverse=True)
lst = [False for i in range(101)]
for num in nums:
    temp = int(num)
    while temp != 1:
        temp = temp // 2 if temp & 1 == 0 else (temp * 3 + 1) // 2
        # 注意temp不要越界
        if temp <= 100:
            lst[temp] = True
flag = False
for item in nums:
    if not lst[int(item)]:
        if not flag:
            print(item, end='')
        else:
            print(' ' + item, end='')
        flag = True
