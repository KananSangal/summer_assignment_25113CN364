// Q6. Write a program to Reverse a number.

#include <stdio.h>
int main()
{
    int num, rem, rev = 0,n;
    printf("Enter a number: ");
    
    if (scanf("%d", &n)==0)
    {
        printf("Invalid input. Please enter a valid integer");
        return 1;
    }
    else
    {
        num=n;
        while (num != 0)
        {
            rem = num % 10;
            rev *= 10;
            rev += rem;
            num/=10;
        }
        printf("The reverse of %d is %d\n", n,rev );
    }
    return 0;
}