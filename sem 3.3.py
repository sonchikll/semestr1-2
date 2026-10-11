a, b = map(int,input().split())
x = 0
y = 0
if a == b:
    print('0', '1', a, end = '')
else:
    while a != b:
        if a > b:
            a = a - b
            x -= 1
        else:
            b = b - a
            y += 1
    print(x,y,a, end = '')