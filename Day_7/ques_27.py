# Q27. Write a program to find Recursive sum of digits.

def recursive_sum(n):
    global ans
    n=abs(n)
    if n==0:
        return
    rem = n%10
    ans += rem 
    return recursive_sum(n//10)

num = int(input("Enter the number: "))
if num==0:
    print(0)
else:
    ans = 0
    recursive_sum(num)
    print(f"The sum of digits of {num} is {ans}.")