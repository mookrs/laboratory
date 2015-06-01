#include <stdio.h>
#define NONBLANK 0

int main(){
    int c, lastc;

    lastc = NONBLANK;
    while((c = getchar()) != EOF){
        if (c != ' '){
            putchar(c);
        }
        else if (lastc != ' '){
            putchar(c); /* 只输出这一次空格 */
        }
        lastc = c;
    }
    return 0;
}