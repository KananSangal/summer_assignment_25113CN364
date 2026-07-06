# Q90 Python Solution

seen=set(); s=input('Enter string: ')
for ch in s:
    if ch in seen: print(ch); break
    seen.add(ch)
else: print('None')
