#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_COLS 20     /* 所能处理的最大列号 */
#define MAX_INPUT 1000  /* 每个输入行的最大宽度 */

int read_column_numbers(int columns[], int max);
void rearrange(char *output, char const *input, int n_columns, int const columns[]);

int main(void)
{
    int n_columns;              /* 进行处理的列标号 */
    int columns[MAX_COLS];      /* 需要处理的列数 */
    char input[MAX_INPUT];      /* 容男输入行的数组 */
    char output[MAX_INPUT];     /* 容纳输出行的数组 */

    n_columns = read_column_numbers(columns, MAX_COLS);

    while (gets(input) != NULL) {
        printf("Original input : %s\n", input);
        rearrange(output, input, n_columns, columns);
        printf("Rearrange line : %s\n", output);
    }

    return EXIT_SUCCESS;
}

/*
** 读取列标号，如果超出规定范围则不予理会。
*/
int read_column_numbers(int columns[], int max)
{
    int num = 0;
    int ch;

    while (num < max && scanf("%d", &columns[num]) == 1 && columns[num] >= 0)
        num += 1;

    if (num % 2 != 0) {
        puts("Last column is not paired.");
        exit(EXIT_FAILURE);
    }

    /* 丢弃该行中包含最后一个数字的那部分内容 */
    while ((ch = getchar()) != EOF && ch != '\n')
        ;

    return num;
}

void rearrange(char *output, char const *input, int n_columns, int const columns[])
{
    int col;        /* columns数组的下标 */
    int output_col; /* 输出列计数器 */
    int len;        /* 输出行的长度 */

    len = strlen(input);
    output_col = 0;

    /* 处理每对列标号 */
    for (col = 0; col < n_columns; col += 2) {
        int nchars = columns[col + 1] - columns[col] + 1;

        /* 如果输入行结束或输出行数组已满，就结束任务 */
        if (columns[col] > len || output_col == MAX_INPUT - 1)
            break;

        /* 如果输出行数据空间不够，只复制可以容纳的数据 */
        if (output_col + nchars > MAX_INPUT - 1)
            nchars = MAX_INPUT - output_col - 1;

        /* 复制相关的数据 */
        strncpy(output + output_col, input + columns[col], nchars);
        output_col += nchars;
    }

    output[output_col] = '\0';
}