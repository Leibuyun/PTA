# 星期要求是A~G的大写字母
# 小时要求的是数字或者A~N的大写字母--它是在第一步之后的
# 分钟要求的是英文字母
s1 = input()
s2 = input()
s3 = input()
s4 = input()
l1, l2, l3, l4 = len(s1), len(s2), len(s3), len(s4)
m1 = l1 if l1 < l2 else l2
i = 0
dayL = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day = 0
while i < m1:
    if s1[i] == s2[i]:
        if ord('A') <= ord(s1[i]) <= ord('G'):
            day = ord(s1[i]) - ord('A')
            break
    i += 1
i += 1
hour = 0
while i < m1:
    if s1[i] == s2[i]:
        if s1[i].isdigit() or ord('A') <= ord(s1[i]) <= ord('N'):
            if s1[i].isdigit():
                hour = int(s1[i])
            else:
                hour = ord(s1[i]) - 65 + 10
            break
    i += 1
i = 0
m2 = l3 if l3 < l4 else l4
minute = 0
while i < m2:
    if s3[i] == s4[i] and s3[i].isalpha():
        minute = i
    i += 1
print(dayL[day], f'{hour:02d}:{minute:02d}')
