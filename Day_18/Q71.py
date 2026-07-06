# Q71 Python Solution

arr=list(map(int,input('Sorted array: ').split())); target=int(input('Target: '))
l,r=0,len(arr)-1
ans=-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target: ans=mid; break
    elif arr[mid]<target: l=mid+1
    else: r=mid-1
print(ans)
