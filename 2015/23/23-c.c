#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define HLF 1
#define TPL 2
#define INC 3
#define JMP 4
#define JIE 5
#define JIO 6
#define END 7

struct instruction {
    int opcode;
    int opcnt;
    int op1, op2;
};

struct instruction *read_program(FILE *fd) {
    char buf[80];
    struct instruction *program;
    int p_ptr = 0;

    program = (struct instruction *) malloc(sizeof(struct instruction) * 100);

    while( fgets(buf, 79, fd) ) {
        struct instruction instr;

        program[p_ptr];
        if( buf[0] == 'h' ) {
            program[p_ptr].opcode = HLF;
            program[p_ptr].opcnt = 1;
            program[p_ptr].op1 = buf[4] - 97;
        } else if( buf[0] == 't' ) {
            program[p_ptr].opcode = TPL;
            program[p_ptr].opcnt = 1;
            program[p_ptr].op1 = buf[4] - 97;
        } else if( buf[0] == 'i' ) {
            program[p_ptr].opcode = INC;
            program[p_ptr].opcnt = 1;
            program[p_ptr].op1 = buf[4] - 97;
        } else if( buf[0] == 'j' ) {
            int n;
            if( buf[2] == 'p' ) {
                program[p_ptr].opcode = JMP;
                program[p_ptr].opcnt = 1;
                sscanf(buf+4, "%d\n", &n);
                program[p_ptr].op1 = n;
            } else if( buf[2] == 'e' ) {
                program[p_ptr].opcode = JIE;
                program[p_ptr].opcnt = 2;
                program[p_ptr].op1 = buf[4] - 97;
                sscanf(buf+7, "%d\n", &n);
                program[p_ptr].op2 = n;
            
            } else if( buf[2] == 'o' ) {
                program[p_ptr].opcode = JIO;
                program[p_ptr].opcnt = 2;
                program[p_ptr].op1 = buf[4] - 97;
                sscanf(buf+7, "%d\n", &n);
                program[p_ptr].op2 = n;
            } else {
                printf("BUG\n");
                exit(1);
            }
        } else {
            printf("BUG\n");
            exit(1);
        }
        p_ptr++;
    }
    program[p_ptr].opcode = END;
    return program;
}

int run_program(struct instruction *prog, unsigned a, unsigned b) {
    int pc = 0; 
    int registers[2];
    int end;

    registers[0] = a;
    registers[1] = b;

    for( end=0; prog[end].opcode != END; ++end )
        ;
    while( (pc >= 0) && (pc < end) ) {
        switch( prog[pc].opcode ) {
            case HLF:
                registers[prog[pc].op1] /= 2;
                pc++;
                break;
            case TPL:
                registers[prog[pc].op1] *= 3;
                pc++;
                break;
            case INC:
                registers[prog[pc].op1] += 1;
                pc++;
                break;
            case JMP:
                pc += prog[pc].op1;
                break;
            case JIE:
                if( (registers[prog[pc].op1] % 2) == 0 )
                    pc += prog[pc].op2;
                else
                    pc++;
                break;
            case JIO:
                if( registers[prog[pc].op1] == 1 )
                    pc += prog[pc].op2;
                else
                    pc++;
                break;
            default:
                printf("BUG\n");
                exit(1);
            
        }
    }
    return registers[1];
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char *fn;
    struct instruction *program, p;
    int i;

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

    program = read_program(fd);
    printf("%d\n", run_program(program, 0, 0));
    printf("%d\n", run_program(program, 1, 0));
}
