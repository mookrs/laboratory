/* 最大子序列和问题 */
#include <stdio.h>

int MaxSubsequenceSum1(const int A[], int N);
int MaxSubsequenceSum2(const int A[], int N);
int Max3(int A, int B, int C);
int MaxSubSum(const int A[], int Left, int Right);
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

int Max3(int A, int B, int C) {
    int max;

    if (A > B)
        if (A > C)
            max = A;
        else
            max = C;
    else if (B > C)
        max = B;
    else
        max = C;

    return max;
}

int MaxSubSum(const int A[], int Left, int Right) {
    int MaxLeftSum, MaxRightSum;
    int MaxLeftBorderSum, MaxRightBorderSum;
    int LeftBorderSum, RightBorderSum;
    int Center, i;

    if (Left == Right) {  /* Base Case */
        if (A[Left] > 0)
            return A[Left];
        else
            return 0;
    }

    Center = (Left + Right) / 2;
    MaxLeftSum = MaxSubSum(A, Left, Center);
    MaxRightSum = MaxSubSum(A, Center + 1, Right);

    MaxLeftBorderSum = 0; LeftBorderSum = 0;
    for (i = Center; i >= Left; --i) {
        LeftBorderSum += A[i];
        if (LeftBorderSum > MaxLeftBorderSum)
            MaxLeftBorderSum = LeftBorderSum;
    }

    MaxRightBorderSum = 0; RightBorderSum = 0;
    for (i = Center + 1; i <= Right; ++i) {
        RightBorderSum += A[i];
        if (RightBorderSum > MaxRightBorderSum)
            MaxRightBorderSum = RightBorderSum;
    }

    return Max3(MaxLeftSum, MaxRightSum, MaxLeftBorderSum + MaxRightBorderSum);
}

int MaxSubsequenceSum3(const int A[], int N) {
    return MaxSubSum(A, 0, N - 1);
}

int MaxSubsequenceSum4(const int A[], int N) {
    int ThisSum, MaxSum, j;

    ThisSum = MaxSum = 0;
    for (j = 0; j < N; ++j) {
        ThisSum += A[j];

        if (ThisSum > MaxSum)
            MaxSum = ThisSum;
        else if (ThisSum < 0)
            ThisSum = 0;
    }
    return MaxSum;
}
