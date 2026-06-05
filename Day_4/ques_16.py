# Q16. Write a program to Print Armstrong numbers in a range.
flag = 0
min = int(input("Enter the lower most number for the range: "))
max = int(input("Enter the upper most number for the range: "))
for num in range(min,max+1,1):
    count=0
    res=0
    n1=num
    while n1!=0: #Counting the number of digits in each number.
        n1//=10
        count+=1
    
    n2=num
    while n2!=0: #Checking if the number is an Armstrong number.
        rem = n2%10
        n2//=10
        res+=rem**count

    if res==num:
        flag=1 #If any Armstrong number is present in the given range.
        print("-->",res,"is an Armstrong number.")
if flag == 0: #If no Armstrong number present in the given range.
    print("--> No Armstrong number present in the given range.")