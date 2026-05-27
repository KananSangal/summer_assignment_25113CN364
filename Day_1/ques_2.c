// Q2. Write a program to Print multiplication table of a given number.

#include <stdio.h>
int main()
{
    int a, i;
    printf("Enter a number: ");
    if (scanf("%d", &a) == 0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1; // All non-zero numbers indicate an error in C.
    }
    else
    {
        printf("You entered the integer: %d\n", a);
        if (a <= 0)
        {
        printf("Negative or zero number entered.\n");
        }
        else
        {
        for (i = 1; i < 11; i++)
        {
            printf("%d * %d = %d\n", a, i, a * i);
        }
        printf("Table of %d is printed.\n", a);
        printf("Thank you!\n");
        }
    }
    return 0;
}       