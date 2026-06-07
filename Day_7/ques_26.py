# Q26. Write a program to find recursive fibonacci series.

def recursive_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return recursive_fib(n-1)+recursive_fib(n-2)

terms = int(input("Enter the number of terms needed: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series: ")
    for i in range(terms):
        print(recursive_fib(i), end=" ")
    print()

    
