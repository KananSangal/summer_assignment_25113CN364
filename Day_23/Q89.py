# Q89 Python Solution

from collections import Counter
s=input('Enter string: '); freq=Counter(s)
for ch in s:
    if freq[ch]==1: print(ch); break
else: print('None')
