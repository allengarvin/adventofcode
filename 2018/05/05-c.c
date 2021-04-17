#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FN argc == 1 ? "05-input.txt" : argv[1]

void process(char *s) {
    for( int i=0; i<strlen(s)-1; i++ )
        if( abs(s[i] - s[i+1]) == 32 )
            s[i] = s[i+1] = ' ';
}

// This method is slow. I should refactor
void compact(char *s) {
    int ptr = 0;

    for( int i=0; i<strlen(s); i++ ) {
        if( s[i] != ' ' )
            s[ptr++] = s[i];
    }
    s[ptr] = 0;
}

int reduce(char *buf) {
    int last_len;

    last_len = strlen(buf);
    buf[strlen(buf)-1] = 0;

    while( strlen(buf) < last_len ) {
        last_len = strlen(buf);
        process(buf);
        compact(buf);
    }
    return strlen(buf);
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *buf, *tmp;
    int last_len, min;

    buf = (char *) malloc(50002);
    tmp = (char *) malloc(50002);
    if( !(fd = fopen(FN, "r")) )
        return printf("%s: cannot open\n", FN), 1;
    fgets(buf, 50002, fd);
    memcpy(tmp, buf, strlen(buf)+1);
    
    reduce(buf);

    printf("%d\n", strlen(buf));

    min = strlen(tmp);
    for( int i=0; i<26; i++ ) {
        int k;

        //printf("Testing %c%c\n", 65+i, 97+i);
        memcpy(buf, tmp, strlen(tmp)+1);
        for( int j=0; j<strlen(buf); j++ ) 
            if( buf[j] == 65 + i || buf[j] == 97 + i )
                buf[j] = ' ';
        compact(buf);

        k = reduce(buf);
        min = k < min ? k : min;
        //printf("%d\n", k);
    }
    printf("%d\n", min);
}
