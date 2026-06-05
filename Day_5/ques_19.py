# Q19. Write a program to Print factors of a number.

num = int(input("Enter the number: "))
if num == 0:
    print("Division of zero is undefined. So NO factors there.")

else:
    fact=[]
    for i in range(1,num+1):
        if (num%i)==0:
            fact.append(i)
    print(f"The factors of the given number {num} is: ",end="")
    print(fact)