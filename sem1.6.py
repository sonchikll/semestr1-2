with open('input.txt', 'r') as f:
    A = list(map(int, f.readline().split()))
    B = f.readline().strip()
    D = int(f.readline().strip())
C = A[0]
for i in A[1:]:
    a = int(str(i), D)
    if B == '+':
        C += a
    elif B  == '-':
        C -= a
    elif B == '*':
        C *= a
l = ""
while C != 0:
    l = str(C % D) + l
    C = C // D
with open('output.txt', 'w') as f:
     f.write(l)