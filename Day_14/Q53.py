# Q53 Python Solution

arr=list(map(int,input('Enter array: ').split())); target=int(input('Target: '))
print(arr.index(target) if target in arr else -1)
