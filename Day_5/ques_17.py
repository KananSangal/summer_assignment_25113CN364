# Q17. Write a program to Check perfect number.

num = int(input("Enter a number to check if it is perfect no. or not: "))
if num == 0:
     print("Zero is not a perfect number.")
else:
     
    res=0

    for i in range (1,num):
        if num%i == 0:
            res += i
        
    if res == num:
            print(f"Yes! {num} is a perfect number.")

    else:
        print(f"No! {num} is not a perfect number.")