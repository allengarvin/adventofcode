#include <stdio.h>
#include <string.h>

int compact(char s[]) {
    int l=0, escape=0;

    for( int i=0; i<strlen(s); i++ ) {
        if( !escape ) {
            if( s[i] == '\"' )
                continue;
            if( s[i] == '\\' ) {
                escape = 1;
                continue;
            }
            l++;
            continue;
        }
        if( s[i] == 'x' ) {
            l += 1;
            i += 2;
        } else
            l++;
        escape = 0;
    }
    return l;
}

int expand(char s[]) {
    int l=2;

    for( int i=0; i<strlen(s); i++ ) {
        if( s[i] == '"' || s[i] == '\\' )
            l += 2;
        else
            l += 1;
    }
    return l;
}

int main() {
    FILE *fd;
    char s[80];
    int part1 = 0, part2 = 0;

    fd = fopen("08-input.txt", "r");
    if( !fd ) 
        return printf("08-input.txt: unable to read\n"), 1;
    
    while( fgets(s, 80, fd ) ) {
        s[strlen(s)-1] = '\0';
        part1 += strlen(s) - compact(s);
        part2 += expand(s) - strlen(s);
    }
    printf("%d\n%d\n", part1, part2);
}
