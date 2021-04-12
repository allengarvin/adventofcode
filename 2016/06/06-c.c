#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    FILE *fd;
    int freqs[8][26] = {0}, max, min, i, j;
    char word[10], code1[9] = {0}, code2[9] = {0};

    if( !(fd = fopen(argc > 1 ? argv[1] : "06-input.txt", "r")) ) {
        fprintf(stderr, "%s: %s\n", argc > 1 ? argv[1] : "06-input.txt", strerror(errno));
        exit(1);
    }
    while( fgets(word, 10, fd) ) {
        for( i=0; i<8; i++ )
            freqs[i][word[i] - 97]++;
    }
    for( i=0; i<8; max = 0, min = 0, i++ ) {
        for( j=0; j<26; j++ ) {
            max = freqs[i][j] > freqs[i][max] ? j : max;
            min = freqs[i][j] < freqs[i][min] ? j : min;
        }
        code1[i] = 97+max;
        code2[i] = 97+min;
    }
    printf("%s\n%s\n", code1, code2);
}
