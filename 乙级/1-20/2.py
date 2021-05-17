s = input()
dic = {
    '0': 'ling',
    '1': 'yi',
    '2': 'er',
    '3': 'san',
    '4': 'si',
    '5': 'wu',
    '6': 'liu',
    '7': 'qi',
    '8': 'ba',
    '9': 'jiu'
}
total = 0
for item in s:
    total += int(item)
s = str(total)
print(dic[s[0]], end='')
for i in range(1, len(s)):
    print(' ' + dic[s[i]], end='')
