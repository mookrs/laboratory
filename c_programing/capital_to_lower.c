#include<stdio.h>

int main(void)
{
    char ch1, ch2;

    scanf("%c", &ch1);
    if (ch1 > 'A' && ch1 <= 'Z')
    {
        ch2 = ch1 + ('a' - 'A');
        printf("%c\n", ch2);
    }
    
    return 0;
}