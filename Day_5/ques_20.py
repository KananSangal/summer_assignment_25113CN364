# Q20. Write a program to find largest prime factor.

num = int(input("Enter the number: "))
if num == 0:
    print("Division of zero is undefined. So NO factors there.")

else:
    large=0
    for i in range(num,1,-1):
        if (num%i)==0:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                large=i
                break

    print(f"The highest prime factor of {num} is: {large}")
