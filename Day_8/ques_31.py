# Q31. Write a program to Print character triangle. 
# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    ascii_val = 65
    for j in range(i):
        print(chr(ascii_val), end="")
        ascii_val += 1
    print()