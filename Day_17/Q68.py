# Q68 Python Solution

a=list(map(int,input('Array 1: ').split())); b=list(map(int,input('Array 2: ').split())); c=list(map(int,input('Array 3: ').split()))
print(list(set(a)&set(b)&set(c)))
