#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int run_test(int n, int part2) {
    int limit, i, j;
    int *arr;

    limit = n / 20;
    arr = (int *) malloc(limit * sizeof(int));
    for( i=0; i<limit; i++ )
        arr[i] = 0;
        
    for( i=1; i<limit; i++ )
        for( j=i; j < (part2 ? (i*50 < limit ? i*50+1 : limit): limit); j += i )
            arr[j] += i * (part2 ? 11 : 10);

    for( int i=0; i<limit; i++ )
        if( arr[i] > n )
            return i;
    return -1;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;
    int n;

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
    fscanf(fd, "%d\n", &n);
    printf("%d\n", run_test(n, 0));
    printf("%d\n", run_test(n, 1));
}
