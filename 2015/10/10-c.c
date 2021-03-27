#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Slow as hell, slower than the python. Todo: rethink
int main() {
    FILE *fd;
    char *num = malloc(20), *tmp, *newnum;
    int len, cnt, i, j;

    fd = fopen("10-input.txt", "r");
    fscanf(fd, "%s", num);
    len = strlen(num);
    newnum = NULL;

    len = strlen(num);

    for( i=1; i<=50; i++ ) {
        char ch;

        tmp = num;
        newnum = realloc(newnum, len * 2 + 1);
        len = 0;

        for( cnt=1; ch = *num; ) {
            if( ch == *++num ) 
                cnt++;
            else {
                sprintf(newnum + len, "%d%c", cnt, ch); 
                len = strlen(newnum);
                cnt = 1;
            }
        }
        num = newnum;
        newnum = tmp;
        //puts(num);
        if( i == 40 )
            printf("%d\n", len);
    }
    printf("%d\n", len);
}
