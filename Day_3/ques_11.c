// Q11. Write a program to Find GCD of two numbers.

#include <stdio.h>
int main()
{
    int a, b, rem;
    printf("Enter the first number: ");
    if (scanf("%d",&a)==0)
    {
        printf("Invalid Input. Please enter a valid integer.\n");
        return 1;
    }
    printf("Enter the second number: ");
    if (scanf("%d", &b)==0)
    {
        printf("Invalid Input. Please enter a valid integer.\n");
        return 1;
    }
    else if ((a==0)&&(b==0))
    {
        printf("The GCD of zeros is zero itself.\n");
        return 1;
    }
    else if ((a==0)||(b==0))
    {
        if (a==0)
        a=b;
    }
    else
    {
        while (b != 0)
        {
            rem = a%b;
            a = b;
            b = rem;
        }
    }
    printf("The GCD of both the numbers is %d\n.", a);
    return 0;
}