#include<stdio.h>
#include<stdlib.h>
#define SIZE 3

struct StudentType
{
    char name[10];
    int num;
    char addr[15];
} stud[SIZE];


int main(void)
{
    FILE *fp;
    int i;

    if ((fp = fopen("stu.dat", "rb")) == NULL)
    {
        printf("Error!\n");
        exit(0);
    }

    for (i = 0; i < SIZE; ++i)
    {
        fread(&stud[i], sizeof(struct StudentType), 1, fp);
        printf("%-10s %-4d %-15s\n", stud[i].name, stud[i].num, stud[i].addr);
    }

    fclose(fp);
    return 0;
}