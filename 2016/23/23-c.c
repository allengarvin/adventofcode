#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CPY 1
#define INC 2
#define DEC 3
#define JNZ 4
#define TGL 5

#define OPERAND_REG 1
#define OPERAND_INT 2

#define OP1 1
#define OP2 2

struct operation {
    int opcode, op_type;
    int op1, op1_type;
    int op2, op2_type;
    int toggled;
};

void run_program(struct operation *prog, int plen, int reg[], char lines[][20]) {
    int pc = 0;

    while( 0 <= pc && pc < plen ) {
        struct operation instr;
        int a, b, offset, nz, apparent_instr;

        if( 0 )
        printf("DEBUG: %2d executing %s %s[reg: %d %d %d %d]\n", 
            pc, lines[pc], prog[pc].toggled ? "(toggled) " : "", 
            reg[0], reg[1], reg[2], reg[3]);
        instr = prog[pc];
        a = instr.op1;
        b = instr.op2;

        if( instr.toggled ) {
            switch( instr.opcode ) {
                case CPY: apparent_instr = JNZ; break;
                case JNZ: apparent_instr = CPY; break;
                case INC: apparent_instr = DEC; break;
                case DEC: apparent_instr = INC; break;
                case TGL:
                    apparent_instr = INC;
                    break;
            }
        } else
            apparent_instr = instr.opcode;

        switch( apparent_instr ) {
            case CPY:
                if( instr.op2_type != OPERAND_INT ) // toggled
                    reg[b] = instr.op1_type == OPERAND_INT ? a : reg[a];
                pc++;
                break;
            case INC:
                reg[a]++;
                pc++;
                break;
            case DEC:
                reg[a]--;
                pc++;
                break;
            case JNZ:
                nz = instr.op1_type == OPERAND_INT ? a : reg[a];
                offset = instr.op2_type == OPERAND_INT ? b : reg[b];
                pc += nz ? offset : 1;
                break;
            case TGL:
                offset = (instr.op1_type == OPERAND_INT ? a : reg[a]) + pc;
                if( offset >= 0 && offset < plen ) {
                    prog[offset].toggled = 1;
                    //printf("TOGGLE %d\n", offset); exit(1);
                } else {
                    //printf("TOGGLE tgl OUTSIDE (%d)\n", offset);
                }
                pc++;
                break;
        }
                
    }
    printf("%d\n", reg[0]);
}

int main(int argc, char *argv[]) {
    struct operation program[50];
    char program_contents[50][20];
    int prog_length, registers[4] = { 7, 0, 0, 0 };    
    char buf[20];
    FILE *fd;

    fd = fopen("23-input.txt", "r");
    for( prog_length = 0; fgets(buf, 19, fd); prog_length++ ) {
        char *opcode;

        buf[strlen(buf)-1] = 0;
        strncpy(program_contents[prog_length], buf, 19);
        opcode = strtok(buf, " ");
        switch( opcode[0] ) {
            case 'c': 
                program[prog_length].opcode = CPY; 
                program[prog_length].op_type = OP2; 
                break; 
            case 't': 
                program[prog_length].opcode = TGL; 
                program[prog_length].op_type = OP1; 
                break; 
            case 'i':
                program[prog_length].opcode = INC; 
                program[prog_length].op_type = OP1; 
                break; 
            case 'd':
                program[prog_length].opcode = DEC; 
                program[prog_length].op_type = OP1; 
                break; 
            case 'j':
                program[prog_length].opcode = JNZ; 
                program[prog_length].op_type = OP2; 
                break; 
            default:
                printf("Unknown operation: %s\n", buf);
                return 1;
        }
        program[prog_length].toggled = 0;

        opcode = strtok(NULL, " ");
        if( opcode[0] >= 97 ) {
            program[prog_length].op1 = opcode[0] - 97;
            program[prog_length].op1_type = OPERAND_REG;
        } else {
            sscanf(opcode, "%d", &program[prog_length].op1);
            program[prog_length].op1_type = OPERAND_INT;
        }
        if( program[prog_length].op_type == OP2 ) {
            opcode = strtok(NULL, " \n");
            if( opcode[0] >= 97 ) {
                program[prog_length].op2 = opcode[0] - 97;
                program[prog_length].op2_type = OPERAND_REG;
            } else {
                sscanf(opcode, "%d", &program[prog_length].op2);
                program[prog_length].op2_type = OPERAND_INT;
            }
        }
    }
    if( argc == 1 )
        registers[0] = 7;
    else
        registers[0] = atoi(argv[1]);
    /*
$ for i in {6..12}; do time ./a.out $i; done
9365

real    0m0.003s
user    0m0.003s
sys     0m0.001s
13685

real    0m0.003s
user    0m0.003s
sys     0m0.001s
48965

real    0m0.008s
user    0m0.004s
sys     0m0.004s
371525

real    0m0.039s
user    0m0.034s
sys     0m0.004s
3637445

real    0m0.332s
user    0m0.331s
sys     0m0.001s
39925445

real    0m3.583s
user    0m3.577s
sys     0m0.001s
479010245

real    0m43.137s
user    0m43.106s
sys     0m0.005s

    I'll optimize it later. I remember solving this originally and
    figuring adding new opcodes into the program, but I can't find it
    */
    run_program(program, prog_length, registers, program_contents);

}
