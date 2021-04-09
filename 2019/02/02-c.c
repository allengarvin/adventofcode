#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define FNAME (argc == 1 ? "02-input.txt" : argv[1])

int program_size = 0;   // dumb, I forgot I needed this to make a copy

char *file_contents(char *fn) {
    FILE *fd;
    struct stat st;
    char *s;

    if( stat(fn, &st) == -1 || !(fd = fopen(fn, "r")) ) {
        fprintf(stderr, "%s: inaccessible\n", fn);
        exit(1);
    }
    s = (char *) malloc(1 + st.st_size * sizeof(char));
    fgets(s, st.st_size, fd);
    return s;
}

int *read_program(char *fn) {
    char *prog, *t;
    int i, cnt = 0;
    int *integers;

    prog = file_contents(fn);
    for( i=0; i<strlen(prog); i++ )
        if( prog[i] == ',' )
            cnt++;

    integers = (int *) malloc(sizeof(int) * cnt);
    for( i = 0, t = strtok(prog, ","); t != NULL; i++, t = strtok(NULL, ",") ) {
        integers[i] = atoi(t);
    }
    program_size = i;
    return integers;
}

#define ADD 1
#define MUL 2
#define HALT 99

int run_program(int *p, int noun, int verb) {
    int opcode, op1, op2, op3, pc = 0, *pcopy, i, result;
    int *prog;

    prog = (int *) malloc(sizeof(int)*program_size);
    for( i=0; i<program_size; i++ )
        prog[i] = p[i];

    prog[1] = noun;
    prog[2] = verb;

    do { 
        int num_args;

        opcode = prog[pc];
        switch( opcode ) {
            case ADD:
            case MUL:
                num_args = 3;
                op1 = prog[prog[pc+1]];
                op2 = prog[prog[pc+2]];
                op3 = prog[pc+3];
                break;
            case HALT:
                num_args = 0;
                break;
            default:
                printf("EXCEPTION: unknown opcode %d (pc = %d)\n", opcode, pc);
                exit(1);
        }

        switch( opcode ) {
            case ADD:
                prog[op3] = op1 + op2;
                break;
            case MUL:
                prog[op3] = op1 * op2;
                break;
            case HALT:
                break;
        }
        pc += num_args + 1;

    } while( opcode != 99 );

    /*
    for( i=0; i<program_size; i++ )
        printf("%d%c", prog[i], i < program_size-1 ? ',' : '\n');
    */
    result = prog[0];
    free(prog);
    return result;
}

int main(int argc, char *argv[]) {
    int *program;
    int result;

    program = read_program(FNAME);
    result = run_program(program, 12, 2);
    printf("%d\n", result);

    for( int i=0; i<1000; i++ )
        for( int j=0; j<1000; j++ )
            if( (result = run_program(program, i, j)) == 19690720 ) {
                printf("%d\n", i * 100 + j);
                return 1;
            }
}
