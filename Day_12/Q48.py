# Q48 Python Solution

def is_perfect(n): return n>0 and sum(i for i in range(1,n) if n%i==0)==n
print(is_perfect(int(input('n: '))))
