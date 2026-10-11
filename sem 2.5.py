A = list(map(int,input().split()))
B = A[-1:] + A[0:-1]
for x in B:
    print(x,end = ' ')