#include <stdio.h>
#include <string.h>
#include <errno.h>

#define ANSWER 2020

int main(int argc, char *argv[]) {
    FILE *fd;
    int n = 0, arr[1000];
    int x, y, z, i;
    int prob1 = 0, prob2 = 0;

    if( argc != 2 ) {
        printf("Usage: %s [file]\n", argv[0]);
        return 1;
    }
    if( (fd = fopen(argv[1], "r")) == NULL ) {
        fprintf(stderr, "%s: %d (%s)\n", argv[1], errno, strerror(errno));
        return 1;
    }
    while( (fscanf(fd, "%d\n", &arr[n]) == 1) && n < 1000  )
        n++;

    if( n == 1000 ) {
        fprintf(stderr, "%s: max int length exceeded", argv[1]);
        return 1;
    }

    for( x=0; x<n && !prob1; x++ )
        for( y=x+1; y<n && !prob1; y++ )
            if( arr[x] + arr[y] == ANSWER ) { 
                printf("Part 1: %d\n", arr[x] * arr[y]);
                prob1 = 1;
            }


    for( x=0; x<n && !prob2; x++ )
        for( y=x+1; y<n && !prob2; y++ )
            for( z=y+1; z<n && !prob2; z++ ) 
                if( arr[x] + arr[y] + arr[z] == ANSWER ) {
                    printf("Part 2: %d\n", arr[x] * arr[y] * arr[z]);
                    return 0;
                }
}
