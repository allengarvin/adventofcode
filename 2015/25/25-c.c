#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

long solve(int r, int c) {
    long start_of_row, start, p1, mod_p;

    start_of_row = (r+c-1) * (r+c-2)/2 + 1;
    start = 20151125;
    p1 = 252533;
    mod_p = 33554393;

    for( int i=0; i<start_of_row + c - 2; i++ )
        start = (start * p1) % mod_p;
    return start;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;
    int row, column;

    if( argc > 1 )
        fn = argv[1];
    else {
        fn = (char *) malloc(13);
        strncat(fn+2, "-input.txt", 12);

        if( isdigit(argv[0][0]) && isdigit(argv[0][1]) && argv[0][2] == '-' ) {
            fn[0] = argv[0][0];
            fn[1] = argv[0][2];
        } else {
            char *buf;
            int i;

            buf = (char *) malloc(80);
            getcwd(buf, 79);
            
            for( i=strlen(buf); i; i-- )
                if( buf[i] == '/' )
                    break;

            if( isdigit(buf[i+1]) && isdigit(buf[i+2]) ) {
                fn[0] = buf[i+1];
                fn[1] = buf[i+2];
            } else {
                fprintf(stderr, "%s: unable to determine input filename from executable or PWD\n", argv[0]);
                return EXIT_FAILURE;
            }
            free(buf);
        }
    }
    fd = fopen(fn, "r");
    if( !fd ) {
        fprintf(stderr, "%s: %s\n", fn, strerror(errno));
        return 1;
    }
    fscanf(fd, "To continue, please consult the code grid in the manual.  Enter the code at row %d, column %d.\n", &row, &column);
    printf("%ld\n", solve(row, column));
}
