#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FN argc == 1 ? "07-input.txt" : argv[1]

#define TYPE_INT 1
#define TYPE_VAR 2
unsigned short variables[676];

struct instruction {
    unsigned short a, b, target;

    int a_type, b_type;
    unsigned short (*func)(unsigned short, unsigned short);
};

unsigned short NOT(unsigned short x, unsigned short _) {
    return 65535 - x;
}

unsigned short ASSIGN(unsigned short a, unsigned short _) {
    return a;
}

unsigned short LSHIFT(unsigned short a, unsigned short b) {
    return (a << b) & 65535;
}

unsigned short RSHIFT(unsigned short a, unsigned short b) {
    return (a >> b) & 65535;
}

unsigned short AND(unsigned short a, unsigned short b) {
    return a & b;
}

unsigned short OR(unsigned short a, unsigned short b) {
    return a | b;
}

struct instruction *parse(char *left, char *right) {
    struct instruction *instr;
    char *a, *b, *c;

    instr = (struct instruction *) malloc(sizeof(struct instruction));

    a = strtok(left, " ");
    b = strtok(NULL, " ");
    c = strtok(NULL, " ");

    if( strlen(right) == 1 )
        instr->target = right[0] - 97;
    else 
        instr->target = (right[0] - 97) * 26 + (right[1] - 97);

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
    }       // ASSIGN

    if( strcmp(a, "NOT") == 0 ) {
         instr->a_type = TYPE_VAR;
         if( strlen(b) == 2 )
            instr->a = (b[0] - 97) * 26 + (b[1] - 97);
         else
            instr->a = b[0] - 97;
        instr->func = &NOT;
        return instr;
    }       // NOT

    // HERE on out we just have arg OPERATION arg

    if( isdigit(a[0]) ) {
        instr->a_type = TYPE_INT;
        instr->a = (unsigned short) atoi(a);
    } else {
        instr->a_type = TYPE_VAR;
        if( strlen(a) == 2 )
            instr->a = (a[0] - 97) * 26 + (a[1] - 97);
        else
            instr->a = a[0] - 97;
    }
    if( isdigit(c[0]) ) {
        instr->b_type = TYPE_INT;
        instr->b = (unsigned short) atoi(c);
    } else {
        instr->b_type = TYPE_VAR;
        if( strlen(c) == 2 )
            instr->b = (c[0] - 97) * 26 + (c[1] - 97);
        else
            instr->b = c[0] - 97;
    }
    if( strcmp(b, "LSHIFT") == 0 ) {
        instr->func = &LSHIFT;
        return instr;
    }
    if( strcmp(b, "RSHIFT") == 0 ) {
        instr->func = &RSHIFT;
        return instr;
    }
    if( strcmp(b, "AND") == 0 ) {
        instr->func = &AND;
        return instr;
    }
    if( strcmp(b, "OR") == 0 ) {
        instr->func = &OR;
        return instr;
    }

    printf("a=<%s> b=<%s> c=<%s>\n", a, b, c);
    return instr;
}

char *print_variable(int n) {
    char *v;

    v = (char *) malloc(3);
    v[2] = 0;
    v[0] = n > 25 ? n / 26 + 97 : 32;
    v[1] = n % 26 + 97;
    return v;
}

void execute(struct instruction *t) {
    int val1, val2;

    if( t->func == NOT ) {
        if( t->a_type == TYPE_INT ) {
            printf("NOT: %s := NOT %d\n", print_variable(t->target), t->a);
            val1 = t->a;
        }
        else {
            val1 = variables[t->a];
            printf("NOT: %s := NOT %s\n", print_variable(t->target), print_variable(t->a));
        }
        variables[t->target] = t->func(val1, 0);
        printf("  Value: %d\n", variables[t->target]);
    }
    if( t->func == ASSIGN ) {
        if( t->a_type == TYPE_INT ) {
            printf("ASSIGN: %s := %d\n", print_variable(t->target), t->a);
            val1 = t->a;
        }
        else {
            val1 = variables[t->a];
            printf("ASSIGN: %s := %s\n", print_variable(t->target), print_variable(t->a));
        }
        variables[t->target] = t->func(val1, 0);
        printf("  Value: %d\n", variables[t->target]);
    }
    if( t->a_type == TYPE_INT )
        val1 = t->a;
    else
        val1 = variables[t->a];
    if( t->b_type == TYPE_INT )
        val2 = t->b;
    else
        val2 = variables[t->b];

    variables[t->target] = t->func(val1, val2);
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[80];
    struct instruction instructs[500], *t;
    int i_ptr = 0;

    for( int i=0; i<676; i++ )
        variables[i] = 0;

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
    for( int i=0; i<676; i++ )
        if( variables[i] )
            printf("%s: %d\n", print_variable(i), variables[i]);

    
}
