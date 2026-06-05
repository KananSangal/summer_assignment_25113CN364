# Q14. Write a program to Find nth Fibonacci term.
print("FIBONACCI GENERATOR")
n = int(input("Enter the value for n to find nth term: "))
a, b = 0, 1

if n <= 0:
    print("Please enter a valid natural number.")
elif n == 1:
    print(1)
else:
    for i in range(3,n+1):
        if (i==n):
            print("The ",n,"th term is: ",a + b, sep="")
            break
        else:
            a,b=b,(a+b)
