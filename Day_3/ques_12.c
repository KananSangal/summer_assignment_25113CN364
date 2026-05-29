// Q12. Write a program to Find LCM of two numbers.

#include <stdio.h>
int main()
{
    int a, b, lcm, max;

    printf("Enter the first no: ");
    if (scanf("%d",&a)==0)
    {
        printf("Invalid Input. Please enter a valid integer.\n");
        return 1;
    }

    printf("Enter the second no: ");
    if (scanf("%d",&b)==0)
    {
        printf("Invalid Input. Please enter a valid integer.\n");
        return 1;
    }
    else if ((a==0)||(b==0))
    {
        printf("The Lcm with zero is undefined.\n");
        return 0;
    }
    else
    {
        max = (a>b)?a:b;
        lcm = max;
        while (1)
        {
            if ((lcm % a ==0) && (lcm % b == 0))
            {
                printf("The LCM of %d and %d is %d.\n", a, b, lcm);
                break;
            }
            lcm += max;
        }
    }
    return 0;
}