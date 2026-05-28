// Q8. Write a program to Check whether a number is palindrome.
// Palindrome is a number whose reverse is equal to that exact number.

#include <stdio.h>
int main()
{
    int num, n, rem, rev=0;
    printf("Enter a number: ");

    if (scanf("%d", &num)==0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    else
    {
        n = num;
        while( n!=0 )
        {
            rem = n%10;
            rev *= 10;
            rev += rem;
            n/=10;
        }
        if (rev == num)
        {
            printf("Yes! The number %d is a palindrome.\n",num);
        }
        else
        {
            printf("No! The number %d is not a palindrome.\n", num);
        }
    }
    return 0;
}