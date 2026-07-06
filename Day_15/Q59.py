# Q59 Python Solution

arr=list(map(int,input('Enter array: ').split())); k=int(input('k: '))%len(arr)
print(arr[-k:]+arr[:-k])
