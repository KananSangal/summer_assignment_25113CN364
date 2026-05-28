// Q5. Write a program to Find sum of digits of a number.

#include <stdio.h>
int main()
{
    int sum = 0, num , rem;
    printf("Enter a number : ");
    if (scanf("%d", &num) == 0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    else
    {
        while (num!=0)
        {
            rem = num % 10;
            sum +=rem;
            num /=10;
        }
        printf("Sum of digits: %d\n", sum);
    }
    return 0;
}