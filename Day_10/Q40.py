# Q40 Python Solution

n=int(input('Enter rows: '))
for i in range(1,n+1): print(' '*(n-i)+''.join(chr(64+j) for j in range(1,i+1))+''.join(chr(64+j) for j in range(i-1,0,-1)))
