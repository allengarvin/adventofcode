#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *run_fill(char *initial, int limit) {
    char *dragon;
    int i, dlen, flag;


    dragon = (char *) malloc(limit+1);
    for( i=0; i<=limit; i++ )
        dragon[i] = 0;

    strncpy(dragon, initial, strlen(initial));
    flag = 1;
    while( flag ) {
        dlen = strlen(dragon);

        dragon[dlen] = 48;

        for( i=0; i<dlen; i++ ) {
            if( i + dlen + 1== limit ) {
                flag = 0;
                break;
            }
            dragon[dlen + i + 1] = dragon[dlen - i - 1] == 48 ? 49 : 48;
        }
    }
    return dragon;
}

char *create_empty_checksum(int d) {
    char *cksum;

    cksum = (char *) malloc(d / 2 + 1);
    for( int i=0; i<=strlen(cksum); ++i )
        cksum[i] = 0;
    return cksum;
}

char *checksum(char *dragon) {
    char *cksum, *tmp;
    int dlen, i;

    do {
        dlen = strlen(dragon);

        cksum = create_empty_checksum(dlen);

        for( int i=0; i<dlen; i += 2 ) {
            cksum[i/2] = dragon[i] == dragon[i+1] ? 49 : 48;
            dragon[i] = dragon[i+1] = 0;
        }
        dragon = cksum;
    } while( strlen(dragon) % 2 == 0 );
    return dragon;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;
    char initial[80];
    char *final, *cksum;

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
    fgets(initial, 79, fd);
    initial[strlen(initial)-1] = 0;

    final = run_fill(initial, 272);
    cksum = checksum(final);
    puts(cksum);

    final = run_fill(initial, 35651584);
    cksum = checksum(final);
    puts(cksum);
}
