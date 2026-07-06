# Q46 Python Solution

def is_armstrong(n):
    return sum(int(d)**len(str(abs(n))) for d in str(abs(n)))==n
print(is_armstrong(int(input('n: '))))
