#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int part1_outer_check(char *ip) {
    int i, n;
    char *next;

    n = strlen(ip);
    next = NULL;

    for( i=0; i<strlen(ip); i++ )
        if( ip[i] == '[' ) {
            n = i;
            next = strchr(ip + i, ']') + 1;
            break;
        }
    for( i=0; i<=n-4; i++ ) {
        if( ip[i] == ip[i+3] && ip[i+1] == ip[i+2] && ip[i] != ip[i+1] )
            return 1;
    }
    if( next == NULL )
        return 0;
    else
        return part1_outer_check(next);
}

int part1_inner_check(char *ip) {
    int i, s, n; 
    char *tmp;

    if( strchr(ip, '[') == NULL )
        return 0;

    for( i=0; i<strlen(ip); i++ ) {
        if( ip[i] == '[' )
            s = i + 1;
        if( ip[i] == ']' ) {
            n = i - s;
            tmp = (char *) malloc(n + 1);
            strncpy(tmp, ip + s, n);
            if( part1_outer_check(tmp) ) {
                return 0;
            }
        }
    }
    return 1;
}

int find_pattern(char *s, char out, char in) {
    for( int i=0; i<=strlen(s)-1; i++ )
        if( s[i] == out && s[i+2] == out && s[i+1] == in )
            return 1;
    return 0;
}

int part2_check2(char *ip, char out, char in) {
    int i, s, n; 
    char *tmp;

    if( strchr(ip, '[') == NULL )
        return 0;

    for( i=0; i<strlen(ip); i++ ) {
        if( ip[i] == '[' )
            s = i + 1;
        if( ip[i] == ']' ) {
            n = i - s;
            tmp = (char *) malloc(n + 1);
            strncpy(tmp, ip + s, n);
            if( find_pattern(tmp, out, in) )
                return 1;
        }
    }
    return 0;
}

int part2_check(char *ip) {
    int i, n;
    char *next;

    n = strlen(ip);
    next = NULL;

    for( i=0; i<=strlen(ip)-2; i++ ) {
        if( ip[i] == '[' ) {
            while( ip[i] != ']' )
                ++i;
            continue;
        }
        if( ip[i] == ip[i+2] && ip[i] != ip[i+1] ) {
            if( part2_check2(ip, ip[i+1], ip[i]) )
                return 1;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn, *ip;
    int part1 = 0, part2 = 0;

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

    ip = (char *) malloc(200);

    while( fgets(ip, 199, fd) ) {
        ip[strlen(ip)-1] = 0;
        if( part1_outer_check(ip) && part1_inner_check(ip) ) {
            ++part1;
        }
        if( part2_check(ip) )
            //puts(ip);
            ++part2;
    }
    printf("%d\n", part1);
    printf("%d\n", part2);
}
