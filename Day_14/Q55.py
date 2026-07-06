# Q55 Python Solution

arr=list(map(int,input('Enter array: ').split()))
unique=sorted(set(arr))
print(unique[-2] if len(unique)>=2 else 'No second largest')
