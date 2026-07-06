# Q60 Python Solution

arr=list(map(int,input('Enter array: ').split()))
res=[x for x in arr if x!=0]+[0]*arr.count(0)
print(res)
