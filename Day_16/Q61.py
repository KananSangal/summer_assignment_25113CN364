# Q61 Python Solution

arr=list(map(int,input('Enter array 0 to n with one missing: ').split()))
n=len(arr)
print(n*(n+1)//2-sum(arr))
