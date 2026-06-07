# Q25. Write a program to Recursive factorial.

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        ans = n * recursive_factorial(n-1)
        return ans
    
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is: {recursive_factorial(num)}")