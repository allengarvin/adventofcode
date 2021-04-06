#include <stdio.h>
#include <stdlib.h>

#define NUM_REGISTERS 16

struct node {
    int registers[NUM_REGISTERS];
    struct node *next;
};

void read_registers(int registers[], char *fn) {
    FILE *fd;

    fd = fopen(fn, "r");
    if( !fd ) {
        fprintf(stderr, "%s: unable to open\n", fn);
        exit(1);
    }
    for( int i=0; EOF != fscanf(fd, "%d ", &registers[i]); i++ ) 
        ;
}

void fill_registers(struct node *n, int registers[]) {
    for( int i=0; i<NUM_REGISTERS; i++ )
        n->registers[i] = registers[i];
}

void show_registers(int registers[]) {
    for( int i=0; i<NUM_REGISTERS; i++ )
        printf("%2d%s", registers[i], i == 15 ? "" : " ");
    puts("");
}

int not_seen(struct node *n, int registers[]) {
    int cnt, i;

    for( cnt = 0; n != NULL; cnt++ ) {
        int eq;

        eq = 1;

        for( i=0; i<NUM_REGISTERS; i++ )
            eq &= (registers[i] == n->registers[i]);
        if( eq )
            return cnt;
        n = n->next;
    }
    return -1;
}

int max_index(int registers[]) {
    int hi_ndx = 0;

    for( int i=0; i<NUM_REGISTERS; i++ )
        if( registers[i] > registers[hi_ndx] )
            hi_ndx = i;
    return hi_ndx;
}

void redistribute(int registers[]) {
    int ndx, hi;

    ndx = max_index(registers);
    hi = registers[ndx];
    registers[ndx] = 0;

    for( int i=(ndx+1)%NUM_REGISTERS; hi; i = (i+1) % NUM_REGISTERS ) {
        registers[i]++;
        hi--;
    }
}

struct node *add_node(struct node *last, int registers[]) {
    struct node *n;

    n = (struct node *) malloc(sizeof(struct node));
    fill_registers(n, registers);
    
    last->next = n;
    n->next = NULL;
    return n;
}

int main(int argc, char *argv[]) {
    int registers[NUM_REGISTERS];
    struct node *first, *last;
    int cnt, part1 = 0;

    read_registers(registers, argc == 1 ? "06-input.txt" : argv[1]);

    first = (struct node *) malloc(sizeof(struct node));
    first->next = NULL;

    fill_registers(first, registers);

    last = first;
    for( cnt=1; ; cnt++ ) {
        redistribute(registers);
        if( not_seen(first, registers) > -1 ) {
            printf("%d\n", cnt);

            if( part1 )
                break;
            else {
                first = last;
                part1 = 1;
                cnt = 1;
            }
        }
        last = add_node(last, registers);
    };
}

