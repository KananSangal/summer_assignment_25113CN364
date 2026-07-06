# Q64 Python Solution

arr=list(map(int,input('Enter array: ').split()))
res=[]
for x in arr:
    if x not in res: res.append(x)
print(res)
