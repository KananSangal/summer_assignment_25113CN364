# Q96 Python Solution

s=input('Enter string: ')
res=''
for ch in s:
    if ch not in res: res+=ch
print(res)
