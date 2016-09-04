/* 选择问题：有一组 N 个数确定其中第 k 个最大者 */
#include <stdio.h>

int find_k_max(int numbers[], int n, int k);
void swap(int *a, int *b);

int main(void) {
    int numbers[] = {8, 23, 47, 4, 35, 11, 59, 41, 1, 29};
    int N = 10;
    int k = N / 2;
    printf("第 k (%d) 个最大者为 %d\n", k, find_k_max(numbers, N, k));

    return 0;
}

int find_k_max(int numbers[], int n, int k) {
    int sorted[k];

    for (int i = 0; i < k; ++i)
        sorted[i] = numbers[i];

    /* 对前 k 个数进行冒泡排序 */
    for (int i = 0; i < k - 1; ++i)
        for (int j = 0; j < k - 1 - i; ++j)
            if (sorted[j] < sorted[j + 1])
                swap(&sorted[j], &sorted[j + 1]);

    for (int i = k; i < n; ++i) {
        int current_number = numbers[i];

        /* {47, 35, 23, 8, 4} */
        /* 11 -> 59 -> 41 -> 1 -> 29 */
        if (current_number < sorted[k-1])
            continue;
        else {
            int j;

            for (j = k - 1; j >= 0; --j)
                if (current_number < sorted[j])
                    break;

            for (int m = k - 1; m > j + 1; --m)
                sorted[m] = sorted[m - 1];

            sorted[j + 1] = current_number;
        }
    }

    return sorted[k - 1];
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
