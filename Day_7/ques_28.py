# Q28. Write a program to find Recursive reverse of a number.

def recursive_rev(n):
    global ans
    n=abs(n)
    if n==0:
        return
    rem = n%10
    ans=(ans*10)+rem
    recursive_rev(n//10)

num = int(input("Enter the number: "))
if num == 0:
    print(f"The reverse of {num} is 0 itself.")
else:
    ans=0
    recursive_rev(num)
    if num<0:
        print(f"The reverse of {num} is -{ans}.")
    else:
        print(f"The reverse of {num} is {ans}.")
