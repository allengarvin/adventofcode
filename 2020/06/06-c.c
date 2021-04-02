#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

// This is the largest number of questions we expect for a single group.
#define MAXBUF 80

char *read_file(char *fn) {
    FILE *fd;
    struct stat buf;
    char *contents;

    if( !(fd = fopen(fn, "r")) ) {
        printf("%s: cannot find\n", fn);
        exit(1);
    }
    stat(fn, &buf);
    
    contents = (char *) malloc(buf.st_size + 1);
    if( fread(contents, 1, buf.st_size, fd) != buf.st_size ) {
        printf("%s: problem reading\n", fn);
        exit(1);
    }
    return contents;
}

int count_splits(char *s) {
    int cnt = 0;

    for( int i=0; i<strlen(s); i++ )
        if( s[i] == '\n' && s[i+1] == '\n' )
            cnt++;
    return cnt;
}

char **split_file(char *s, int nn) {
    char **r, *last;
    int i, j, r_ptr = 0, len;

    r = (char **) malloc(nn * sizeof(char *) + 1);
    r[r_ptr++] = s;

    len = strlen(s);
    for( i = 0; i<len; i++ ) {
        if( s[i] == '\n' && s[i-1] == '\n' ) {
            s[i] = 0;
            r[r_ptr++] = &s[i+1];
            i++;
            last = &s[i];
        }
    }
    for( i=0; i<len; i++ )
        if( s[i] == '\n' )
            s[i] = ' ';
    r[r_ptr++] = last;
    return r;
}

void do_union(char buf[], char *tok) {
    int i, j, uflag;

    for( i=0; i<strlen(tok); i++ ) {
        for( uflag = 1, j=0; j<strlen(buf); j++ )
            if( buf[j] == tok[i] ) {
                uflag = 0;
                break;
            }
        if( uflag )
            buf[strlen(buf)] = tok[i];
    }
}

void do_intersection(char buf[], char *tok) {
    int i, j, t_ptr = 0, iflag;
    char *tmp;

    tmp = (char *) malloc(MAXBUF * sizeof(char));
    for( i=0; i<MAXBUF; i++ )
        tmp[i] = 0;    

    for( i=0; i<strlen(tok); i++ ) {
        for( iflag = 0, j=0; j<strlen(buf); j++ )
            if( buf[j] == tok[i] ) {
                iflag = 1;
                break;
            }
        if( iflag )
            tmp[t_ptr++] = tok[i];
    }
    for( i=0; i<MAXBUF; i++ )
        buf[i] = i < t_ptr ? tmp[i] : 0;
        
}

int main(int argc, char *argv[]) {
    char *con, **records, union_buf[MAXBUF], intersection_buf[80], *tok;
    int i, j, k, count, u_count = 0, i_count = 0;

    con = read_file(argc == 1 ? "06-input.txt" : argv[1]);
    count = count_splits(con) + 1;
    records = split_file(con, count);

    for( i=0; i<count; i++ ) {
        for( j=0; j<MAXBUF; j++ )
            union_buf[j] = intersection_buf[j] = 0;

        tok = strtok(records[i], " ");
        strncpy(union_buf, tok, strlen(tok));
        strncpy(intersection_buf, tok, strlen(tok));

        for( tok = strtok(NULL, " "); tok != NULL; tok = strtok(NULL, " ") ) {
            do_union(union_buf, tok);
            do_intersection(intersection_buf, tok);
        }
        u_count += strlen(union_buf);
        i_count += strlen(intersection_buf);
    }
    printf("%d\n", u_count);
    printf("%d\n", i_count);
}
