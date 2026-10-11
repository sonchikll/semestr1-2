A = list(map(int,input().split()))
c = 0
for x in A:
    if A.count(x) > c:
        c = A.count(x)
for x in A:
    if A.count(x) == c:
        print(x)
        break