/* Tower of Hanoi */
/* 要求：将A中的圆盘借助B圆盘完全移动到C圆盘上，每次只能移动一个圆盘，并且每次移动时大盘不能放在小盘上面 */

/*
状态0 A：n个盘子。B：空的。C：空的。
状态1 A：第n个盘子。B：n-1个盘子。C：空的。
中间状态 A：空的。B：n-1个盘子。C：第n个盘子。
中间状态 A：空的。B：n-1个盘子。C：（可看作）空的。
状态2 A：n-1个盘子。B：空的。C：第n个盘子（可看作空的）。
*/

/*
1. if n==1, move the single disk from A to C and stop.
2. Move the top n-1 disks from A to B, using C as auxiliary.
3. Move the remaining disk from A to C.
4. Move the n-1 disks from B to C, using A as auxiliary.
*/

/* For n disks, total 2^n – 1 moves are required. */

#include <stdio.h>

void move(int, char, char, char);

int main(void)
{
    int num;
    printf("Enter number of plates: ");
    scanf("%d", &num);
    
    move(num, 'A', 'B', 'C');
    return 0;
}

void move(int num, char A, char B, char C){
    /* If only 1 disk, make the move and return */
    if (num == 1) {
        printf("\nMove disk %d from peg %c to peg %c", num, A, C);
    } else {
        /* Move top n-1 disks from A to B, using C as auxiliary */
        move(num - 1, A, C, B);
        /* Move remaining disks from A to C */
        printf("\nMove disk %d from peg %c to peg %c", num, A, C);
        /* Move n-1 disks from B to C using A as auxiliary */
        move(num - 1, B, A, C);
    }
}