# Q56 Python Solution

arr=list(map(int,input('Enter array: ').split()))
seen=set(); dup=set()
for x in arr:
    if x in seen: dup.add(x)
    seen.add(x)
print(list(dup))
