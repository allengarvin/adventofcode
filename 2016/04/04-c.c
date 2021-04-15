#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int valid1(char *l, char *ck) {
    int alphabet[26] = {0};
    char check[6] = {0};
    int max, i, j;

    for( i=0; i<strlen(l); i++ )
        if( l[i] != '-' )
            alphabet[l[i]-97]++;

    for( i=0; i<5; i++ ) {
        max = 0;
        for( j=0; j<26; j++ )
            if( alphabet[max] < alphabet[j] )
                max = j;
        check[i] = 97 + max;
        alphabet[max] = 0;
    }
    return strncmp(ck, check, 5) == 0;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[80], letters[80], cksum[6];
    int ndx, i, j, total = 0, vault = -1;

    fd = fopen("04-input.txt", "r");
    if( !fd ) {
        printf("04-input.txt: cannot open\n");
        return 1;
    }
    while( fgets(buf, 79, fd) ) {
        buf[strlen(buf)-1] = 0;

        for( j = 0, i=strlen(buf); i; --i ) {
            if( buf[i] == '[' ) {
                strncpy(cksum, buf + i + 1, 5);
                buf[i] = 0;
                j = i;
            }
            if( j && buf[i] == '-' ) {
                ndx = atoi(buf + i + 1);
                strncpy(letters, buf, i);
                letters[i] = 0;
                break;
            }
                
        }
        if( valid1(letters, cksum) ) {
            total += ndx;
            for( int i=0; i<strlen(letters); i++ )
                letters[i] = letters[i] == '-' ? ' ' : (((letters[i] - 97) + ndx) % 26) + 97;
            if( strstr(letters, "northpole") != NULL )
                vault = ndx;
        }
    }
    printf("%d\n", total);
    printf("%d\n", vault);
}
    
