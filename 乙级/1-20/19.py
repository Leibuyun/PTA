n = int(input())


def allSame(num):
    a, b, c, d = num % 10, num // 10 % 10, num // 100 % 10, num // 1000
    return a == b and a == c and a == d


def getNum(num, flag):
    lst = [num % 10, num // 10 % 10, num // 100 % 10, num // 1000]
    lst.sort(reverse=flag)
    return lst[0] * 1000 + lst[1] * 100 + lst[2] * 10 + lst[3]


if allSame(n):
    print(f'{n:04d} - {n:04d} = 0000')
else:
    maxNum = getNum(n, True)
    minNum = getNum(n, False)
    temp = maxNum - minNum
    while temp != 6174:
        print(f'{maxNum:04d} - {minNum:04d} = {(maxNum - minNum):04d}')
        maxNum = getNum(temp, True)
        minNum = getNum(temp, False)
        temp = maxNum - minNum
    print(f'{maxNum:04d} - {minNum:04d} = {(maxNum - minNum):04d}')
