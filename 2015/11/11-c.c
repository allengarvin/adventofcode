#include <stdio.h>
#include <math.h> // remember to link -lm
#include <stdlib.h>
#include <string.h>

long to_integer(char *p) {
    long num = 0, pow = 1;

    for( int i=strlen(p)-1; i >= 0; pow *= 26, i-- )
        num += (long) (p[i] - 97) * pow;
    return num;
}

char *to_string(long n) {
    char *c;
    int i, sz;

    sz = round(log(n) / log(26.0));
    c = (char *) malloc( sz * sizeof(char *) + 1);
    c[sz] = '\0';
    for( i=0; n > 0; i++ ) {
        c[sz-i] = n % 26 + 97;
        n /= 26;
    }
    return c;
}

int test_passwd(char *p) {
    int seq = 0, dub1 = -1, dub2 = 0;

    for( int i=0; i<strlen(p); i++ ) {
        if( p[i] == 'i' || p[i] == 'o' || p[i] == 'l' )
            return 0;
        if( i<strlen(p)-1 && p[i] == p[i+1] ) {
            if( dub1 == -1 )
                dub1 = i;
            else if( i > dub1+1 )
                dub2 = i;
        }
        if( i<strlen(p)-1 && p[i] == p[i+1]-1 && p[i] == p[i+2]-2 )
            seq = 1;
    }
    return seq && dub1 > -1 && dub2;
}

int main() {
    FILE *fd;
    char passwd[21], *p;
    long p_num;
    int cnt = 0;
    
    fd = fopen("11-input.txt", "r");
    if( !fd )
        return 1;
    
    fgets(passwd, 20, fd);
    passwd[strlen(passwd)-1] = '\0';

    p_num = to_integer(passwd);
    for( long i = p_num; cnt < 2; i++ ) {
        p = to_string(i);
        if( test_passwd(p) ) {
            printf("%s\n", p);
            cnt++;
        }
    }
}
    
