#include <stdio.h>
#define NotFound -1
typedef int ElementType;

int BinarySearch(const ElementType A[], ElementType X, int N);

int main(void) {
    int sequence[] = {-4, -2, -1, 0, 2, 4, 5};
    printf("%d\n", BinarySearch(sequence, 2, 7));
    printf("%d\n", BinarySearch(sequence, 1, 7));

    return 0;
}

/* 对分查找 */
int BinarySearch(const ElementType A[], ElementType X, int N) {
    int Low, Mid, High;

    Low = 0; High = N - 1;
    while (Low <= High) {
        Mid = (Low + High) / 2;
        if (A[Mid] < X)
            Low = Mid + 1;
        else if (A[Mid] > X)
            High = Mid - 1;
        else
            return Mid;
    }
    return NotFound;
}

