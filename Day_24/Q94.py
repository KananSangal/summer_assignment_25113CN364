# Q94 Python Solution

s=input('Enter string: ')
res=''; i=0
while i<len(s):
    count=1
    while i+1<len(s) and s[i]==s[i+1]: count+=1; i+=1
    res+=s[i]+str(count); i+=1
print(res)
