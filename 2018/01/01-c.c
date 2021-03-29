#include <stdio.h>
#include <stdlib.h>

#define MAXBUF 1000000
#define OFFSET 100000

// Doesn't work in general case but I'm lazy. We'll just pick a big number and see if we get a segfault
int freq_repeat(int f, int buffer[]) {
    if( buffer[OFFSET + f] ) {
        printf("%d\n", f);
        exit(1);
    }
    buffer[OFFSET + f] = 1;
    return 0;
}

int main() {
    FILE *fd;
    int n, numbers[1024], n_ptr = 0, freq=0, buffer[MAXBUF] = {0};
    

    if( !(fd = fopen("01-input.txt", "r")) )
        return fprintf(stderr, "01-input: unable to open\n"), 1;
    
    while( fscanf(fd, "%d", &numbers[n_ptr]) != EOF )
        n_ptr++;
    
    for( int i=0; i < MAXBUF && !freq_repeat(freq, buffer); i++ ) {
        freq += numbers[i % n_ptr];
        if( i == n_ptr - 1 ) 
            printf("%d\n", freq);
    }
}

    
