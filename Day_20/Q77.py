# Q77 Python Solution

r1=int(input('Rows A: ')); c1=int(input('Cols A / Rows B: ')); c2=int(input('Cols B: '))
A=[list(map(int,input().split())) for _ in range(r1)]
B=[list(map(int,input().split())) for _ in range(c1)]
C=[[sum(A[i][k]*B[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
for row in C: print(row)
