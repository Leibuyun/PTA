"""
值得注意的点：
    ①答案正确， 由递归来定义。答案正确后导出的答案也是正确的， 由上一个正确的答案， 按照规则， 下一个也是正确的
    ②这里我采用字符串分割的方法, a = re.spilit('P|T'),
      只有当len(a)==3, 并且P在T之前， 并且a[0] * len(a[1]) == a[2], a[1]!=''的时候， 字符串才是正确的！
"""
n = int(input())
for i in range(n):
    string = input()
    flag = True
    for item in string:
        if not (item == 'P' or item == 'A' or item == 'T'):
            flag = False
            break
    if not flag:
        print('NO')
        continue
    import re
    a = re.split(r'P|T', string)
    if len(a) == 3 and a[0] * len(a[1]) == a[2] and a[1] != '' and string.find('P') < string.find('T'):
        print('YES')
    else:
        print('NO')
