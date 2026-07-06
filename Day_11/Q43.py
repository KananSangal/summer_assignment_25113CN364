# Q43 Python Solution

def is_prime(n):
    return n>=2 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
print('Prime' if is_prime(int(input('n: '))) else 'Not Prime')
