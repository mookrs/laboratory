/* 最大子序列和问题 */
#include <stdio.h>

int MaxSubsequenceSum1(const int A[], int N);
int MaxSubsequenceSum2(const int A[], int N);
int MaxSubsequenceSum3(const int A[], int N);
int MaxSubsequenceSum4(const int A[], int N);

int main(void) {
    int sequence[] = { -5, 1, 5, -4, 5, 9, -3, 2, 2, -3 };

    printf("%d\n", MaxSubsequenceSum1(sequence, 10));
    printf("%d\n", MaxSubsequenceSum2(sequence, 10));
    printf("%d\n", MaxSubsequenceSum3(sequence, 10));
    printf("%d\n", MaxSubsequenceSum4(sequence, 10));
}

int MaxSubsequenceSum1(const int A[], int N) {
    int ThisSum, MaxSum, i, j, k;

    MaxSum = 0;
    for (i = 0; i < N; ++i) {
        for (j = i; j < N; ++j) {
            ThisSum = 0;
            for (k = i; k <= j; ++k)
                ThisSum += A[k];

            if (ThisSum > MaxSum)
                MaxSum = ThisSum;
        }
    }
    return MaxSum;
}

int MaxSubsequenceSum2(const int A[], int N) {
    int ThisSum, MaxSum, i, j, k;

    MaxSum = 0;
    for (i = 0; i < N; ++i) {
        ThisSum = 0;
        for (int j = i; j < N; ++j) {
            ThisSum += A[j];

            if (ThisSum > MaxSum)
                MaxSum = ThisSum;
        }
    }
    return MaxSum;
}

int MaxSubsequenceSum3(const int A[], int N) {
    return 0;

}

int MaxSubsequenceSum4(const int A[], int N) {
    return 0;

}
