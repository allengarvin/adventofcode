#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define XOR(A,B) !(A) != !(B)

int main() {
    FILE *fd;
    int part1 = 0, part2 = 0;

    char passwd[80];
    int a, b;
    char c;

    if( !(fd = fopen("02-input.txt", "r")) )
        return 1;

    while( fscanf(fd, "%d-%d %c: %s", &a, &b, &c, &passwd) != EOF ) {
        int count, i;

        for( i=0, count=0; i<strlen(passwd); i++ ) {
            if( passwd[i] == c )
                count++;
        }

        if ( a <= count && count <= b )
            part1++;
        if ( XOR(passwd[a-1] == c, passwd[b-1] == c) )
            part2++;
        
    }
    printf("%d\n%d\n", part1, part2);
}
    
