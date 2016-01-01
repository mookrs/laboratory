#include<stdio.h>
#define SIZE 3

struct StudentType
{
    char name[10];
    int num;
    char addr[15];
} stud[SIZE];

void save()
{
    FILE *fp;
    int i;

    if((fp = fopen("stu.dat", "wb")) == NULL)
    {
        printf("Can't open.\n");
        return;
    }
    for (i = 0; i < SIZE; ++i)
    {
        if(fwrite(&stud[i], sizeof(struct StudentType), 1, fp) != 1)
        {
            printf("File write error!");
        }
    }
    fclose(fp);
}

int main(void)
{
    int i;
    printf("Please input data:\n");
    for (i = 0; i < SIZE; ++i)
    {
        scanf("%s %d %s", stud[i].name, &stud[i].num, stud[i].addr);
    }
    save();
    
    return 0;
}