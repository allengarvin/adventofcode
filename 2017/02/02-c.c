#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void read_sheet(int sheet[16][16], char *fn) {
    FILE *fd;
    char s[80];

    fd = fopen(fn, "r");
    if( !fd ) {
        fprintf(stderr, "%s: %s\n", fn, strerror(errno));
        exit(1);
    }
    for( int j=0; fgets(s, 79, fd); j++ ) {
        char *tmp;
        int i, d;

        //printf("%s\n", s);
        for( i = 0, tmp = strtok(s, " "); tmp; tmp = strtok(NULL, " ") ) {
            sscanf(tmp, "%d\n", &d);
            sheet[j][i] = d;
            i++;
        }
    }
}

int max(int row[16]) {
    int maxint = -1; 

    for( int i=0; i<16; i++ )
        maxint = maxint > row[i] ? maxint : row[i];
    return maxint;
}

int min(int row[16]) {
    int minint = 0x7fffffff; 

    for( int i=0; i<16; i++ )
        minint = minint < row[i] ? minint : row[i];
    return minint;
}

int checksum(int sheet[16][16]) {
    int cksum = 0;

    for( int i=0; i<16; i++ ) {
        cksum += max(sheet[i]) - min(sheet[i]);
    }
    return cksum;
}

int divisible(int row[16]) {
    for( int i=0; i<16; i++ )
        for( int j=i+1; j<16; j++ ) {
            if( row[j] > row[i] ) {
                if( row[j] % row[i] == 0 )
                    return row[j] / row[i];
            } else {
                if( row[i] % row[j] == 0 )
                    return row[i] / row[j];
            }
        }
    return 0;
}

int divisible_sum(int sheet[16][16]) {
    int cksum = 0;

    for( int i=0; i<16; i++ )
        cksum += divisible(sheet[i]);
    return cksum;
}

int main(int argc, char *argv[]) {
    int sheet[16][16] = { 0 };

    read_sheet(sheet, argc == 1 ? "02-input.txt" : argv[1]);
    printf("%d\n", checksum(sheet));
    printf("%d\n", divisible_sum(sheet));
}
