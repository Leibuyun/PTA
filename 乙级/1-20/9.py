string = input()
words = reversed(string.split())
print(next(words), end='')
for word in words:
    print('', word, end='')
