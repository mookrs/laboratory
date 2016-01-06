/* 选择问题：有一组N个数确定其中第k个最大者 */
#include <stdio.h>

int find_k_max(int numbers[], n, k);
void swap(int *a, int *b);

int main(void) {
    int numbers[] = {8, 23, 47, 4, 35, 11, 59, 41, 1, 29};
    int N = 10;
    int k = N / 2;
    printf("第 k 个最大者为 %d\n", find_k_max(numbers, N, k));

    return 0;
}

int find_k_max(int numbers[], n, k) {
    int sorted[k];

    for (int i = 0; i < k; ++i)
        sorted[i] = numbers[i];

    for (int i = 0; i < k - 1; ++i)
        for (int j = i; j < k - 1; ++j)
            if (sorted[j] < sorted[j + 1])
                swap(sorted[j], sorted[j + 1]);

    for (int i = k; i < n; ++i)
    {
        int current_number = numbers[i];
        int j = k - 1;
        while (current_number > sorted[j]) {
            /*TODO*/
        }
    }

    return sorted[k - 1];
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}