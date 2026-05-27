// Q4. Write a program to Count digits in a number.

#include <stdio.h>
int main()
{
    int num, count = 0;
    printf("Enter a number: ");
    if (scanf("%d", &num) == 0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    else
    {
        while (num != 0)
        {
            num /= 10;
            count++;
        }
    }
    printf("Number of digits: %d\n", count);
    return 0;
}