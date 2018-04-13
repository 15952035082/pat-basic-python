input_s = input()
res = 0
table = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
for i in range(0, len(input_s)):
    res += int(input_s[i])
ss = str(res)
for i in range(0, len(ss)):
    print(table[int(ss[i])], sep='', end='')
    if i != len(ss)-1:
        print(' ', end='')
