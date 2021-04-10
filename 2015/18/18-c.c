#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

#define NW(X) grid[(X)-101]
#define N(X)  grid[(X)-100]
#define NE(X) grid[(X)-99]
#define W(X)  grid[(X)-1]
#define E(X)  grid[(X)+1]
#define SW(X) grid[(X)+99]
#define S(X)  grid[(X)+100]
#define SE(X) grid[(X)+101]

char *file_contents(char *fn) {
    FILE *fd;
    struct stat st;
    char *s;

    if( stat(fn, &st) == -1 || !(fd = fopen(fn, "r")) ) {
        fprintf(stderr, "%s: inaccessible\n", fn);
        exit(1);
    }
    s = (char *) malloc(1 + st.st_size * sizeof(char));
    fread(s, st.st_size, sizeof(char), fd);
    s[st.st_size-1] = 0;
    return s;
}

int *read_file(char *fn) {
    char *fcon;
    int *grid;
    int ptr = 0;

    grid = (int *) malloc(sizeof(int)*100*100);
    fcon = file_contents(fn);
    for( int i = 0; i<strlen(fcon); i++ ) {
        switch( fcon[i] ) {
            case '#': grid[ptr++] = 1; break;
            case '.': grid[ptr++] = 0; break;
        }
    }
    return grid;
}

int *intdup(int *src, int sz) {
    int *dst = (int *) malloc(sz * sizeof(int));
    memcpy(dst, src, sz * sizeof(int));
    return dst;
}

int run(int *grid, int steps, int part2p) {
    int *ngrid, i, j, cnt;

    for( cnt=0, i=0; i<10000; i++ )
        cnt += grid[i];

    for( i=0; i<steps; i++ ) {
        if( part2p )
            grid[0] = grid[99] = grid[9999] = grid[9900] = 1;
        ngrid = (int *) malloc(sizeof(int) * 100*100);
        for( j=0; j<10000; j++ ) {
            int x, y;

            x = j % 100;
            y = j / 100;
            
            cnt = 0;
            if( y > 0 ) {
                if( x > 0 )
                    cnt += NW(j);
                cnt += N(j);
                if( x < 99 )
                    cnt += NE(j);
            }
            if( x > 0 )
                cnt += W(j);
            if( x < 99 )
                cnt += E(j);
            if( y < 99 ) {
                if( x > 0 )
                    cnt += SW(j);
                cnt += S(j);
                if( x < 99 )
                    cnt += SE(j);
            }
            if( grid[j] == 1 )
                ngrid[j] = (cnt == 2 || cnt == 3) ? 1 : 0;
            else
                ngrid[j] = cnt == 3 ? 1 : 0;
        }

        for( cnt=0, j=0; j<10000; j++ ) {
            cnt += ngrid[j];
        }
        free(grid);
        grid = ngrid;
    }
    if( part2p )
        grid[0] = grid[99] = grid[9999] = grid[9900] = 1;

    for( cnt=0, i=0; i<10000; i++ )
        cnt += grid[i];
    return cnt;
}

int main(int argc, char *argv[]) {
    int *grid;

    grid = read_file(argc == 1 ? "18-input.txt" : argv[1]);
    printf("%d\n", run(intdup(grid, 100*100), 100, 0));
    printf("%d\n", run(intdup(grid, 100*100), 100, 1));
}
