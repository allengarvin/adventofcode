#include <stdio.h>
#include <stdlib.h>

#define MAX 30000000
int main(int argc, char argv[]) {
    FILE *fd;
    int *previous;
    int n;
    int cnt = 0, next_seq;

    previous = (int *) malloc(MAX * sizeof(int));

    for( int i=0; i<MAX+1; i++ )
        previous[i] = -1;
    fd = fopen("15-input.txt", "r");
    if( !fd )
        return printf("15-input.txt: cannot open\n"), EXIT_FAILURE;

    while( fscanf(fd, "%d", &n) ) {
        previous[n] = cnt++;
        if( fgetc(fd) != ',' )
            break;
    }

    next_seq = 0;
    while( 1 ) {
        int last, prev;

        last = next_seq;
        prev = previous[next_seq];
        next_seq = cnt - (prev == -1 ? cnt : prev);
        previous[last] = cnt;

        ++cnt;
        if( cnt + 1 == 2020 )
            printf("%d\n", next_seq);
        if( cnt + 1 == MAX ) {
            printf("%d\n", next_seq);
            break;
        }
    }
    
}

