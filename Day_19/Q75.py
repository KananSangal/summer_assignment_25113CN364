# Q75 Python Solution

r=int(input('Rows: ')); c=int(input('Cols: '))
A=[list(map(int,input().split())) for _ in range(r)]
for j in range(c): print([A[i][j] for i in range(r)])
