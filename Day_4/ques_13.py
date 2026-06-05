# Q13. Write a program to generate Fibonacci series.
print("FIBONACCI GENERATOR")
num = int(input("Enter the number of terms you want for your fibonacci: "))
a, b = 0, 1

if num <= 0:
    print("Enter a positive integer")
elif num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(0,(num-2),1):
        print(a + b)
        a,b=b,(a+b)
