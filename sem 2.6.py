A = list(map(int,input().split()))
for x in A:
    if A.count(x) == 1:
        print(x, end = ' ')