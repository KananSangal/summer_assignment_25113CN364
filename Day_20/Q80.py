# Q80 Python Solution

r=int(input('Rows: ')); c=int(input('Cols: '))
A=[list(map(int,input().split())) for _ in range(r)]
for j in range(c): print(sum(A[i][j] for i in range(r)))
