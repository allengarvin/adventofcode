#include <stdio.h>
#include <string.h>

int check_string1(char *s) {
    int vwlcnt = 0; 
    int dbl = 0, bad_str = 0;
    char bads[4][3] = { "ab", "cd", "pq", "xy" }, tmp[3];
    
    tmp[2] = '\0';

    for( int i=0; i<strlen(s); i++ ) {
        switch( s[i] ) {
            case 'a': 
            case 'e': 
            case 'i': 
            case 'o':
            case 'u': vwlcnt++;
        }
        if( s[i] == s[i+1] ) 
            dbl = 1;
        strncpy(tmp, s + i, 2);
        for( int j=0; j<4; j++ ) 
            if( strcmp(tmp, bads[j]) == 0 )
                bad_str = 1;
    }
    
    return vwlcnt >= 3 && dbl && !bad_str;
}

int check_string2(char *s) {
    int pair = 0, middle = 0;
    for( int i=0; i<strlen(s)-1; i++ ) {
        for( int j=i+2; j<strlen(s); j++ ) 
            if( s[i] == s[j] && s[i+1] == s[j+1] )
                pair = 1;
        if( s[i] == s[i+2] )
            middle = 1;
    }
    return pair && middle;
}

int main() {
    FILE *fd;
    char str[20];
    int total1 = 0, total2 = 0;

    fd = fopen("05-input.txt", "r");
    if( !fd ) {
        fprintf(stderr, "05-input: unable to open\n");
        return 1;
    }
    while( fgets(str, 18, fd ) ) {
        str[strlen(str)-1] = '\0';
        total1 += check_string1(str);
        total2 += check_string2(str);
    }
    printf("%d\n%d\n", total1, total2);
}
    
