#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int ascendingp(char *s) {
    for( int i=0; i<strlen(s)-1; i++ )
        if( s[i] > s[i+1] )
            return 0;
    return 1;
}

int doublep(char *s) {
    for( int i=0; i<strlen(s)-1; i++ )
        if( s[i] == s[i+1] )
            return 1;
    return 0;
}

int triplep(char *s) {
    for( int i=0; i<strlen(s); i++ )
        if( s[i] == s[i+1] )
            if( (i == 0 || s[i-1] != s[i]) && (s[i+2] != s[i]) )
                return 0;
            else
                i++;
    return 1;
}

int main(int argc, char *argv) {
    FILE *fd;
    char *tmp;
    int lo, hi, cnt = 0, cnt2 = 0;

    if( !(fd = fopen("04-input.txt", "r")) )
        return printf("04-input.txt: unable to open\n"), 1;

    fscanf(fd, "%d-%d\n", &lo, &hi);
    tmp = (char *) malloc(sizeof(char) * 7);

    for( int i=lo; i <= hi; i++ ) {
        sprintf(tmp, "%d", i);
        if( ascendingp(tmp) && doublep(tmp) ) {
            cnt++;
            if( !triplep(tmp) )
                cnt2++;
        }
    }
    printf("%d\n", cnt);
    printf("%d\n", cnt2);
}
