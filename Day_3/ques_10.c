// Q10. Write a program to print prime numbers in a range.

#include <stdio.h>
int main()
{
    int max, num,j, min, flag=0,prime=0;

    printf("Enter the minimum number of the range: ");
    if (scanf("%d",&min)==0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    printf("Enter the maximum number of the range: ");
    if (scanf("%d",&max)==0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    for (num=min;num<=max;num++)
    {
        if (num>1)
        {
            flag =0;
            for (j=2;j<num;j++)
            {
                if (num%j==0)
                {
                    flag = 1;
                    break;
                }
            }
            if (flag ==0)
            {
                printf("The number %d is a prime number.\n", num);
                prime+=1;
            }
        }
    }
    if (prime==0)
    {
        printf("There is no prime number present in the given range.\n");
    }
    return 0;
}