# Q22. Write a program to convert binary number to decimal.

num = input("Enter binary number: ")
frac=""
if "." in str(num):
    num,frac=str(num).split(".")
    num=int(num)
    frac=int(frac)
else:
    num=int(num)
count=0
n=num
mul=1
dec=0
while num!=0:
    count+=1
    num//=10

for i in range(count-1,-1,-1):
    dec += int(str(n)[i]) * mul
    mul*=2
if frac!="":
    f=frac
    count=0
    ans_frac=0
    mul = 2**(-1)
    while f!=0:
        count+=1
        f//=10
    for i in range(count):
        ans_frac += int(str(frac)[i]) * mul
        mul*=(2**(-1))

    print(dec+ans_frac)

else:
    print(dec)





