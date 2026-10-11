A = list(map(int,input().split()))
for i in range (1, A[0]+1):
    if i not in A[1:]:
        print(i)
        break