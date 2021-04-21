#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void process(char s[]) {
    int level = 0, grp = 0, score = 0, skip = 0, garbage = 0, garbage_c = 0;
    int scores[100];
    
    for( int i=0; i<strlen(s); i++ ) {
        char ch;

        ch = s[i];

        if( ch == '!' && !skip )
            skip = 1;
        else if( skip )
            skip = 0;
        else if( garbage ) {
            if( ch == '>' )
                garbage = 0;
            else
                garbage_c++;
        } else if( ch == '<' )
            garbage = 1;
        else if( ch == '{' ) {
            scores[level] = level+1;
            level++;
            grp++;
        } else if( ch == '}' ) {
            score += scores[--level];
        }
    }
    printf("%d\n%d\n", score, garbage_c);
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;
    char buf[32768];

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
    fread(buf, 32767, 1, fd);
    buf[strlen(buf)-1] = 0;
    process(buf);
}
