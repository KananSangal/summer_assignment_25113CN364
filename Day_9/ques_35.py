# Q35. Write a program to Print repeated character pattern.
# A
# BB
# CCC
# DDDD
# EEEEE

n=int(input("Enter the number of rows: "))
ascii=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ascii),end="")
    ascii+=1
    print()