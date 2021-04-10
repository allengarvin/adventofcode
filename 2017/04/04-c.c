#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct passphrase {
    char **words;
    int wordcnt;
};

int compare(const void *a, const void *b) {
    if( *(char *) a != *(char *) b )
        return *(char *)a - *(char *)b;
    return 0;
}

int equality(char *a, char *b) {
    return !strncmp(a, b, strlen(a));
}

int anagram(char *a, char *b) {
    qsort(a, strlen(a), 1, compare);
    qsort(b, strlen(b), 1, compare);
    return equality(a, b);
}

int check_valid(struct passphrase *pp, int (*checker_function)(char *,char *)) {
    for( int i=0; i<pp->wordcnt; i++ )
        for( int j=i+1; j<pp->wordcnt; j++ ) {
            if( strlen(pp->words[j]) != strlen(pp->words[i]) )
                continue;
            if( checker_function(pp->words[i], pp->words[j]) )
                return 0;
        }
    return 1;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[80];
    struct passphrase pp;
    int cnt, part1 = 0, part2 = 0;

    if( !(fd = fopen(argc == 1 ? "04-input.txt" : argv[1], "r")) )
        return puts("Unable to open input file"), 1;

    while( fgets(buf, 80, fd) != NULL ) {
        buf[strlen(buf)-1] = 0;

        char *tok;
        int ptr;

        cnt = 1;
        for( int i=0; i<strlen(buf); i++ )
            if( buf[i] == ' ' )
                cnt++;
        pp.wordcnt = cnt;
        pp.words = (char **) malloc(sizeof(char *) * cnt);

        ptr = 0;
        for( tok = strtok(buf, " "); tok != NULL; tok = strtok(NULL, " "), ptr++ ) {
            pp.words[ptr] = (char *) malloc(sizeof(char) * strlen(tok)+1);
            strncpy(pp.words[ptr], tok, strlen(tok)+1);
        }
        if( check_valid(&pp, &equality) ) {
            part1++;
            if( check_valid(&pp, &anagram) )
                part2++;
        }
    }
    printf("%d\n%d\n", part1, part2);
}
