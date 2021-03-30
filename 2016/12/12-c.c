#include <string.h>
#include <stdio.h>

#define CPY 1
#define INC 2
#define DEC 3
#define JNZ 4

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
        int a, b, test;

        //printf("DEBUG: executing %s [reg: %d %d %d %d\n", lines[pc], reg[0], reg[1], reg[2], reg[3]);
        instr = prog[pc];
        a = instr.op1;
        b = instr.op2;
        switch( instr.opcode ) {
            case CPY:
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
                test = instr.op1_type == OPERAND_INT ? a : reg[a];
                pc += test ? instr.op2 : 1;
                break;
        }
                
    }
    printf("%d\n", reg[0]);
}

int main(int argc, char *argv[]) {
    struct operation program[50];
    char program_contents[50][20];
    int prog_length, registers[4] = { 0, 0, 0, 0 };    
    char buf[20];
    FILE *fd;

    fd = fopen("12-input.txt", "r");
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
    run_program(program, prog_length, registers, program_contents);
    registers[0] = 0;
    registers[1] = 0;
    registers[2] = 1;
    registers[3] = 0;
    run_program(program, prog_length, registers, program_contents);
}
