# Q83 Python Solution

s=input('Enter string: ')
v=sum(1 for ch in s.lower() if ch in 'aeiou')
c=sum(1 for ch in s.lower() if ch.isalpha() and ch not in 'aeiou')
print('Vowels =',v,'Consonants =',c)
