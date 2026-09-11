with open('input.txt', 'r') as f:
    A = list(map(float, f.readline().split()))
    B = f.readline().strip()

C = A[0]
for a in A[1:]:
    if B == '+':
        C += a
    elif B  == '-':
        C -= a
    elif B == '*':
        C *= a
with open('output.txt', 'w') as f:
     f.write(str(result))