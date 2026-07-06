# Q78 Python Solution

n=int(input('Size: '))
A=[list(map(int,input().split())) for _ in range(n)]
print('Symmetric' if all(A[i][j]==A[j][i] for i in range(n) for j in range(n)) else 'Not Symmetric')
