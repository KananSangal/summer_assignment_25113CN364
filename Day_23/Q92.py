# Q92 Python Solution

from collections import Counter
s=input('Enter string: ')
print(Counter(s).most_common(1)[0][0])
