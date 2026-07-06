# Q63 Python Solution

arr=list(map(int,input('Enter array: ').split())); target=int(input('Target sum: '))
seen=set(); found=False
for x in arr:
    if target-x in seen:
        print(target-x,x); found=True; break
    seen.add(x)
if not found: print('No pair')
