#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int base26_conv(char *s) {
    int n;
    char c;

    n = 0;
    while( c = *s++ )
        n = n * 26 + (c - 96);

    return n;
}

void run_instructions(FILE *fd) {
    char buf[80];
    int *registers = (int *) malloc(26*26*26 * sizeof(int));
    int i, part2 = -1, part1 = -1;

    for( i=0; i<26*26*26; i++ )
        registers[i] = 0;

    while( fgets(buf, 79, fd) ) {
        char *r1, *r2, *instr, *test;
        int val1, val2;
        int ndx1, ndx2;
        int test_result;

        r1 = strtok(buf, " ");
        instr = strtok(NULL, " ");
        val1 = atoi(strtok(NULL, " "));

        strtok(NULL, " ");

        r2 = strtok(NULL, " ");
        test = strtok(NULL, " ");
        val2 = atoi(strtok(NULL, " "));

        base26_conv("aaa");

        ndx1 = base26_conv(r1);
        ndx2 = base26_conv(r2);

        test_result = 0;
        if( strcmp(test, "==") == 0 )      test_result = registers[ndx2] == val2;
        else if( strcmp(test, ">=") == 0 ) test_result = registers[ndx2] >= val2;
        else if( strcmp(test, "<=") == 0 ) test_result = registers[ndx2] <= val2;
        else if( strcmp(test, "!=") == 0 ) test_result = registers[ndx2] != val2;
        else if( strcmp(test, ">") == 0 )  test_result = registers[ndx2] > val2;
        else if( strcmp(test, "<") == 0 )  test_result = registers[ndx2] < val2;
        else { printf("BUG: %s\n", test); exit(1); }
        if( test_result ) {
            if( strcmp(instr, "inc") == 0 )
                registers[ndx1] += val1;
            else if( strcmp(instr, "dec") == 0 )
                registers[ndx1] -= val1;
            if( registers[ndx1] > part2 )   
                part2 = registers[ndx1];
        }
    }
    for( i=0; i<26*26*26; i++ )
        part1 = registers[i] > part1 ? registers[i] : part1;
    printf("%d\n%d\n", part1, part2);
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;

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
    run_instructions(fd);
}
