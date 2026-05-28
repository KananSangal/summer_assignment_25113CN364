// Q7. Write a program to find product of digits.

#include <stdio.h>
int main()
{
    int num, prod = 1,rem, n;
    printf("Enter a number: ");

    if (scanf("%d", &num)==0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    else if (num == 0)
    { printf( "The product of digits is 0.\n");}
    else
    {
        n = num;
        while (n != 0)
        {
            rem = n%10;
            prod *= rem;
            n/=10;
        }
        printf("The product of digits of %d is %d.\n", num, prod);
    }
    return 0;
}