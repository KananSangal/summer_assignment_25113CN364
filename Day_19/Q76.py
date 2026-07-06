# Q76 Python Solution

n=int(input('Size: '))
A=[list(map(int,input().split())) for _ in range(n)]
print(sum(A[i][i] for i in range(n)))
