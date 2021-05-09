lst = input().split()[1:]
a1 = a2 = a3 = a4 = a5 = cnt4 = cnt2 = 0
for num in lst:
    num = int(num)
    remainder = num % 5
    if remainder == 0:
        if num & 1 == 0:
            a1 += num
    elif remainder == 1:
        a2 += num if cnt2 & 1 == 0 else -num
        cnt2 += 1
    elif remainder == 2:
        a3 += 1
    elif remainder == 3:
        cnt4 += 1
        a4 += num
    else:
        if num > a5:
            a5 = num

# 注意a2由于是交错求和， 和数可能为0， 需要用cnt2来判断
print(a1 if a1 != 0 else 'N', a2 if cnt2 != 0 else 'N', a3 if a3 != 0 else 'N', f'{a4 / cnt4:.1f}' if a4 != 0 else 'N',
      a5 if a5 != 0 else 'N')
