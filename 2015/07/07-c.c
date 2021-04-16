#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FN argc == 1 ? "07-input.txt" : argv[1]

#define TYPE_INT 1
#define TYPE_VAR 2
struct instruction {
    unsigned short a, b, target;

    int a_type;
    unsigned short (*func)(unsigned short, unsigned short);
};

unsigned short NOT(unsigned short x, unsigned short _) {
    return 65535 - x;
}

unsigned short ASSIGN(unsigned short a, unsigned short __) {
    return a;
}


struct instruction *parse(char *left, char *right) {
    struct instruction *instr;
    char *a, *b, *c;

    instr = (struct instruction *) malloc(sizeof(struct instruction));

    a = strtok(left, " ");
    b = strtok(NULL, " ");
    c = strtok(NULL, " ");

    if( !b && !c ) {
        if( isdigit(a[0]) ) {
            instr->a_type = TYPE_INT;
            instr->a = atoi(a);
        } else {
            instr->a_type = TYPE_VAR;
            if( strlen(a) == 2 )
                instr->a = (a[0] - 97) * 26 + (a[1] - 97);
            else
                instr->a = a[0] - 97;
        }
        instr->func = &ASSIGN;
        return instr;
    }
    if( isdigit(a[0]) ) {
        instr->a_type = TYPE_INT;
        instr->a = (unsigned short) atoi(a);
    } else if( strcmp(a, "NOT") == 0 ) {
         instr->a_type = TYPE_VAR;
         if( strlen(b) == 2 )
            instr->a = (b[0] - 97) * 26 + (b[1] - 97);
         else
            instr->a = b[0] - 97;
        instr->func = &NOT;
        return instr;
    } else {
        instr->a_type = TYPE_VAR;
        if( strlen(a) == 2 )
            instr->a = (a[0] - 97) * 26 + (a[1] - 97);
        else
            instr->a = a[0] - 97;
    }
    printf("a=<%s> b=<%s> c=<%s>\n", a, b, c);
    return instr;
}

void execute(struct instruction *t) {
    if( t->func == NOT ) {
        printf("NOT\n");
    }
    if( t->func == ASSIGN ) {
        printf("ASSIGN\n");
    }
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[80];
    struct instruction instructs[500], *t;
    int i_ptr = 0;

    if( !(fd = fopen(FN, "r")) ) {
        fprintf(stderr, "%s: %s\n", FN, strerror(errno));
        return 1;
    }

    while( fgets(buf, 80, fd) ) {
        char *left, *right;
        int i;

        buf[strlen(buf)-1] = 0;

        for( i=0; i<strlen(buf); i++ )
            if( buf[i] == '-' )
                break;

        buf[i-1] = 0;
        left = buf;
        right = buf + i + 3;
        
        //instructs[i++] = *parse(left, right);
        t = parse(left, right);
        execute(t);
    }

    
}
