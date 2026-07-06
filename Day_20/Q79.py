# Q79 Python Solution

r=int(input('Rows: ')); c=int(input('Cols: '))
A=[list(map(int,input().split())) for _ in range(r)]
for row in A: print(sum(row))
