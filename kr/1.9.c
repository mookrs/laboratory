#include <stdio.h>
#define NONBLANK 0

int main(){
    int c, lastc;
    lastc = NONBLANK;

    while((c = getchar()) != EOF){
        if (c != ' '){
            putchar(c);
        }
        else{
            if (lastc != ' '){
                /* 只输出这一次空格 */
                putchar(c);
            }
        }
        lastc = c;
    }

    return 0;
}