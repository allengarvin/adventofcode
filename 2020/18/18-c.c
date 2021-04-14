/* It's been like 20+ years since I wrote a recursive descent parser! 
   I used a subset of one I wrote in Pike in the 90s for this. */
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TYPE    long

#define L_PAREN 10
#define R_PAREN 11
#define ADD     12
#define MUL     13
#define WHITE   254
#define ERROR   255
    
struct tokenized {
    int num_tokens;
    long tokens[200];
    int current_token;
};

long expr(struct tokenized *t, int part2);

void fatal(char *str) {
    fprintf(stderr, "FATAL: %s\n", str);
    exit(1);
}

TYPE char_to_token(char c) {
    if( isdigit(c) )
        return c - 48;

    switch( c ) {
        case '(': return L_PAREN;
        case ')': return R_PAREN;
        case '+': return ADD;
        case '*': return MUL;
        case ' ':
        case '\t': return WHITE;
        default:  return ERROR;
    }
}

struct tokenized *tokenize(char *buf) {
    struct tokenized *t;

    t = (struct tokenized *) malloc(sizeof(struct tokenized));
    t->num_tokens = 0;
    t->current_token = 0;
    for( long i=0; i<strlen(buf); i++ ) {
        TYPE n;

        n = char_to_token(buf[i]);
        switch( n ) {
            case WHITE:
                continue;
            case ERROR:
                printf("Unexpected char: `%c'\n", buf[i]);
                exit(1);
            default:
                t->tokens[t->num_tokens++] = n;
                break;
        }
    }
    return t;
}

long current_token(struct tokenized *t) {
    return t->tokens[t->current_token];
}

long eat_token(struct tokenized *t) {
    return t->tokens[++t->current_token];
}

long token_available(struct tokenized *t) {
    return t->current_token < t->num_tokens;
}

long primary(struct tokenized *t, int part2) {
    TYPE m;
    long second;

    if( !token_available(t) ) {
        printf("ERROR: primary expected\n");
        exit(1);
    }
    m = current_token(t);
    switch( m ) {
        case ADD: fatal("Unexpected `+'");
        case MUL: fatal("Unexpected `*'");
        case R_PAREN: fatal("Unexpected `)'");
        case L_PAREN:
            eat_token(t);
            second = expr(t, part2);
            if( !token_available(t) )
                fatal("Unterminated `('");
            if( current_token(t) != R_PAREN )
                fatal("Expected `)'");
            eat_token(t);
            return second;
        default:
            eat_token(t);
            return (long) m;
    }
}

long term(struct tokenized *t, int part2) {
    long left = primary(t, part2);

    while( 1 ) {
        TYPE m;

        if( !token_available(t) )
            return left;
        m = current_token(t);

        switch( m ) {
            case ADD:
                eat_token(t);
                left += primary(t, part2);
                break;
            default:
                return left;
        }
    }
}

long expr(struct tokenized *t, int part2) {
    long left; 

    if( part2 )
        left = term(t, part2);
    else
        left = primary(t, part2);

    while( 1 ) {
        TYPE m;

        if( !token_available(t) )
            return left;
        m = current_token(t);

        if( part2 ) {
            switch( m ) {
                case MUL:
                    eat_token(t);
                    left *= term(t, 1);
                    break;
                default:
                    return left;
            }
        } else {
            switch( m ) {
                case ADD:
                    eat_token(t);
                    left += primary(t, 0);
                    break;
                case MUL:
                    eat_token(t);
                    left *= primary(t, 0);
                    break;
                default:
                    return left;
            }
        }
    }
}

void show_tokens(struct tokenized *t, char *buf) {
    printf("%s\n", buf);
    for( long i=0; i<t->num_tokens; i++ )
        switch( t->tokens[i] ) {
            case L_PAREN: putchar('('); break;
            case R_PAREN: putchar(')'); break;
            case MUL:     putchar('*'); break;
            case ADD:     putchar('+'); break;
            default:      putchar(48 + t->tokens[i]);
        }
    printf("\n");
}

long main(long argc, char *argv[]) {
    FILE *fd;
    char buf[200];
    long total1 = 0, total2 = 0;

    if( argc == 2 && strcmp("stdin", argv[1]) == 0 )
        fd = stdin;
    else {
        fd = fopen(argc == 1 ? "18-input.txt" : argv[1], "r");
        if( !fd ) {
            fprintf(stderr, "%s: %s\n", argc == 1 ? "18-input.txt" : argv[1], strerror(errno));
            return 1;
        }
    }
    while( fgets(buf, 199, fd) ) {
        struct tokenized *tokens;
        long val1, val2;

        buf[strlen(buf)-1] = 0;
        tokens = tokenize(buf);
        //show_tokens(tokens, buf);

        val1 = expr(tokens, 0);
        tokens->current_token = 0;
        val2 = expr(tokens, 1);

        total1 += val1;
        total2 += val2;

    }
    printf("%ld\n", total1);
    printf("%ld\n", total2);
}

