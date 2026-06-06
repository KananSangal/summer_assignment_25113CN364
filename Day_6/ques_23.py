# Q23. Write a program to count set bits in a number.

num_dec = input("Enter a decimal number: ")
if float(num_dec) == 0.0:
    print("0")
else:
    num_frac=""
    if "." in num_dec:
        num_dec, num_frac = num_dec.split(".")
        num_dec = int(num_dec)
        num_frac = float("."+num_frac)
    else:
        num_dec = int(num_dec)

    flag = 1
    ans=0
    while (num_dec>0):
        rem = num_dec % 2
        num_dec = num_dec // 2
        ans += (flag*rem)
        flag *=10
    if num_frac != "":
        mul = 1
        ans_frac = 0
        for _ in range(5):
            rem = num_frac * 2
            dec,num_frac = int(rem), rem-int(rem)
            ans_frac += int(dec)*mul
            mul *= 10
        res=(f"{ans}.{ans_frac}")
    else:
        res=(ans)

    count = res.count("1")
    print(f"Set bits: {count}")


