# Q15. Write a program to Check Armstrong number.

print("""\nAn Armstrong number is a positive integer
that equals the sum of its own digits, each raised
to the power of the total number of digits in the number.\n""")

num = int( input ("Enter the number to check if it is armstrong or not: "))

count=0
num_2=0

n=num
while (num!=0):
    num = num // 10
    count+=1

print("\nThere are ",count," digits in the given number.\n",sep="")

n1=n
while (n!=0):
    rem = n % 10
    n = n // 10
    num_2 += rem**count

print("The sum of the digits of the given no. each raised to the power of",count,"is:",num_2,"\n")

if (n1 == num_2):
    print("So, Yes! ",n1," is an Armstrong number.\n", sep="")
else:
    print("So, No! ",n1," is not an Armstrong number.\n", sep="")