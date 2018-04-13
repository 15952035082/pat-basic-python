x = int(input())
step = 0
while x != 1:
    step += 1
    if x % 2 == 0:
        x /= 2
    else:
        x = 3*x + 1
        x /= 2
print(step, end='')
