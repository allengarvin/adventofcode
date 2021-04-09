#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define FNAME (argc == 1 ? "07-input.txt" : argv[1])

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
    int i, cnt = 1;
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

#define ADD         1
#define MUL         2
#define INPUT       3
#define OUTPUT      4
#define JNZ         5
#define JZ          6
#define LT          7
#define EQ          8
#define HALT 99

int run_program(int *p, int input[], int break_on_output) {
    int opcode, op1, op2, op3, pc = 0, *pcopy, i, result, input_ptr = 0, jump_flag = 0;
    int mask, mask1, mask2, mask3, output;
    int *prog;

    prog = (int *) malloc(sizeof(int)*program_size);
    for( i=0; i<program_size; i++ )
        prog[i] = p[i];

    do { 
        int num_args;

        opcode = prog[pc] % 100;
        mask = prog[pc] / 100;
        mask1 = mask % 10;
        mask /= 10;
        mask2 = mask % 10;
        mask /= 10;
        mask3 = mask % 10;
   
        switch( opcode ) {
            case ADD:
            case MUL:
            case EQ:
            case LT:
                num_args = 3;
                op1 = mask1 ? prog[pc+1] : prog[prog[pc+1]];
                op2 = mask2 ? prog[pc+2] : prog[prog[pc+2]];
                op3 = prog[pc+3]; // Parameters that an instruction writes to will never be in immediate mode.
                if( mask3 ) {
                    printf("EXCEPTION: %d,%d,%d,%d (opcode=%02d, mask=%03d)\n", 
                        prog[pc], prog[pc+1], prog[pc+2], prog[pc] % 100, prog[pc] / 100);
                    printf("  Parameters that an instruction writes to will never be in immediate mode.\n");
                    exit(1);
                }
                break;
            case JNZ:
            case JZ:
                num_args = 2;
                op1 = mask1 ? prog[pc+1] : prog[prog[pc+1]];
                op2 = mask2 ? prog[pc+2] : prog[prog[pc+2]];
                num_args = 2;
                break; 
            case INPUT:
                num_args = 1;
                op1 = prog[pc+1];
                break;
            case OUTPUT:
                num_args = 1;
                op1 = mask1 ? prog[pc+1] : prog[prog[pc+1]];
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
            case LT:
                prog[op3] = op1 < op2 ? 1 : 0;
                break;
            case EQ:
                prog[op3] = op1 == op2 ? 1 : 0;
                break;
            case JNZ:
                if( op1 ) {
                    pc = op2;
                    jump_flag = 1;
                }
                break;
            case JZ:
                if( op1 == 0 ) {
                    pc = op2;
                    jump_flag = 1;
                }
                break;
            case INPUT:
                prog[op1] = input[input_ptr++];
                break;
            case OUTPUT:
                if( break_on_output )
                    return op1;
                else
                    output = op1;
                break;
            case HALT:
                break;
        }
        if( jump_flag )
            jump_flag = 0;      // Jump already made
        else
            pc += num_args + 1;
    } while( opcode != 99 );

    /*
    for( i=0; i<program_size; i++ )
        printf("%d%c", prog[i], i < program_size-1 ? ',' : '\n');
    */
    return output;
}

// Ugly but workable code from Rosetta code
char **permute5() {
    char a[6] = "43210";  //array
    int i, j;
    int f=120;      //factorial
    int ndx = 0;
    char c;          //buffer
    char **permutations;

    permutations = (char **) malloc(sizeof(char *) * 120);

    while (f--) {
        permutations[ndx] = (char *) malloc(6 * sizeof(char));
        strncpy(permutations[ndx], a, 6);
        i=1;
        while(a[i] > a[i-1]) i++;
        j=0;
        while(a[j] < a[i])j++;
        c=a[j];
        a[j]=a[i];
        a[i]=c;
        i--;
        for (j = 0; j < i; i--, j++) {
            c = a[i];
            a[i] = a[j];
            a[j] = c;
        }
        ndx++;
    }
    return permutations;
}


int main(int argc, char *argv[]) {
    int *program;
    int result;
    int input[2];
    int max = -1;
    char **permutations;

    program = read_program(FNAME);

    permutations = permute5();

    for( int i=0; i<120; i++ ) {
        result = 0; // 2nd input for first amplifier
        for( int j=0; j<5; j++ ) {
            input[0] = permutations[i][j] - '0';
            input[1] = result;

            result = run_program(program, input, 1);
        }
        if( result > max ) {
            max = result;
        }
    }
    printf("%d\n", max);
    // Oh crud, I need a whole different mechanism for interprocess communication, with
    // blocking for part 2. Putting that off for now
}
