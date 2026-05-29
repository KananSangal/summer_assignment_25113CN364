// Q9. Write a program to Check whether a number is prime.

#include <stdio.h>
int main()
{
    int num,i;

    printf("Enter a number to check: ");

    if (scanf("%d",&num)==0)
    {
        printf("Invalid input. Please enter a valid integer.\n");
        return 1;
    }
    else if (num==0 || num==1)
    {
        printf("%d is neither prime nor a composite number.\n", num);
    }
    else
    {
        for (i=num-1;i>1;i--)
        {
            if ((num%i)==0)
            {
               printf("The Number %d is not Prime.\n", num);
               return 0; 
            }
        }
        printf("The number %d is Prime\n", num);
    }
    return 0;
}