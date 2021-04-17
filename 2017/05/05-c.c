#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int run_program(int *program, int prog_size, bool part2) {
    int *prog;
    int steps = 0, jmp;


    prog = (int *) malloc(sizeof(int) * prog_size);
    memcpy(prog, program, prog_size * sizeof(int));

    for( int pc=0; pc >= 0 && pc < prog_size; ++steps) {
        jmp = prog[pc];
        if( jmp >= 3 && part2 )
            prog[pc]--;
        else 
            prog[pc]++;
        if( jmp )
            pc += jmp;

    }
    return steps;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn, *line;
    int *program, ndx;

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

    program = (int *) malloc(sizeof(int) * 2048);

    for( ndx = 0; EOF != fscanf(fd, "%d\n", &program[ndx]); ndx++ )
        ;

    printf("%d\n", run_program(program, ndx, false));
    printf("%d\n", run_program(program, ndx, true));
}
