// Q3. Write a program to Find factorial of a number.

#include <stdio.h>
int main()
{
    int a, i,fact = 1;
    printf("Enter a number: ");

    if (scanf("%d", &a) == 0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1; // All non-zero numbers indicate an error in C.
    }
    else if (a < 0)
    {
        printf("Factorial is not defined for negative numbers.\n");
        return 1;
    }
    else if (a == 0 || a == 1)
    {
        printf("Factorial of %d is 1.\n", a);
        return 0;
    }
    else
    {
        fact = a;
        for (i = a - 1; i > 0; i--)
        {
            fact *= i;
        }
        printf("Factorial of %d is %d.\n", a, fact);
    }
    return 0;
}