#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

#define ACC 0
#define JMP 1
#define NOP 2

#define TOGGLE(X) X->opcode == JMP ? (X->opcode = NOP) : (X->opcode = JMP)

struct Node {
    int opcode, operand;
    struct Node *next;
};

struct Node *mknode(int opcode, int operand) {
    struct Node *n;

    n = (struct Node *) malloc(sizeof(struct Node));
    n->opcode = opcode;
    n->operand = operand;
    n->next = NULL; 
    return n;
}

void show_program(struct Node *n) {
    int i=0; 

    while( n != NULL ) {
        switch( n->opcode ) {
            case 0: printf("[%3d] acc ", i); break;
            case 1: printf("[%3d] jmp ", i); break;
            case 2: printf("[%3d] nop ", i); break;
        }
        i++;
        if( n->operand > 0 )
            printf("+");
        printf("%d\n", n->operand);
        n = n->next;
    }
}

int run_program(struct Node *program[], int size, int part2_flag) {
    int line_hit[size], pc = 0, acc = 0;
    for( int i=0; i<size; i++ )
        line_hit[i] = 0;
    
    while( pc < size && line_hit[pc] == 0 ) {
        int opc, oper;

        opc = program[pc]->opcode;
        oper = program[pc]->operand;
        line_hit[pc] = 1;
        switch( opc ) {
            case ACC: acc += oper; break;
            case NOP: break;
            case JMP: pc += oper; break;
        }
        if( opc != JMP )
            pc++;

    }    
    if( part2_flag && pc >= 0 && pc < size )
        return -1;

    return acc;
}

int main(int argc, char *argv[]) {
    struct Node *first, *last;
    int llist_size = 0, operand, *instruction_hits;
    char line[40], opcode[3];
    int part2_changes[1000], part2_sz = 0, part1, part2;
    FILE *fd;

    if( !(fd = fopen(argc == 1 ? "08-input.txt" : argv[1], "r")) ) {
        fprintf(stderr, "%s: unable to open file\n", argc == 1 ? "08-input.txt" : argv[1]);
        return 1;
    }
    while( fgets(line, 20, fd) != NULL ) {
        int code;

        sscanf(line, "%s %d\n", opcode, &operand);
        if( strcmp(opcode, "jmp") == 0 ) {
            code = JMP;
            part2_changes[part2_sz++] = llist_size;
        } else if( strcmp(opcode, "acc") == 0 ) {
            code = ACC;
        } else if( strcmp(opcode, "nop") == 0 ) {
            code = NOP;
            part2_changes[part2_sz++] = llist_size;
        }
        else {
            fprintf(stderr, "Unknown opcode: %s\n", line);
            return 1;
        }

        if( llist_size == 0 ) {
            last = first = mknode(code, operand);
        } else {
            last->next = mknode(code, operand);
            last = last->next;
        }

        llist_size += 1;
    }

    struct Node *program[llist_size], *n;
    n = first;
    for( int i=0; i<llist_size; i++ ) {
        program[i] = n;
        n = n->next;
    }
    part1 = run_program(program, llist_size, FALSE);
    printf("%d\n", part1);
    for( int i=0; i<part2_sz; i++ ) {
        TOGGLE(program[part2_changes[i]]);
        part2 = run_program(program, llist_size, TRUE);
        TOGGLE(program[part2_changes[i]]);
        if( part2 > -1 )
            break;
    }
    printf("%d\n", part2);
}
    

    
