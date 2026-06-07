"""Q36. Write a program to Print hollow square pattern.
*****
*   *
*   *
*   *
*****"""

n=int(input("Enter the side of square: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1):
            print("*",end="")
        elif j==0 or j==(n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()