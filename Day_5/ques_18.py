# Q18. Write a program to Check strong number.
print("A STRONG NUMBER is a number which is equal to the sum of factorial of its individual digits.\n")
num = int(input("Enter a number to check if it is a strong number or not: "))
res = 0
n=num

if (num==0):
    print("No! Zero is not a strong number.")
else:
    while (num!=0):
        rem = num %10
        num //=10
        fact=1
        for i in range (1,(rem+1)):
            fact *= i
        res+=fact

    if res == n:
        print(f"Yes, {n} is a strong number.")
    else:
        print(f"No, {n} is not a strong number.")
