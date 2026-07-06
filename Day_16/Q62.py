# Q62 Python Solution

from collections import Counter
arr=list(map(int,input('Enter array: ').split()))
print(Counter(arr).most_common(1)[0][0])
