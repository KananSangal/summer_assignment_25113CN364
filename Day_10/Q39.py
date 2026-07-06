# Q39 Python Solution

n=int(input('Enter rows: '))
for i in range(1,n+1): print(' '*(n-i)+''.join(str(j) for j in range(1,i+1))+''.join(str(j) for j in range(i-1,0,-1)))
