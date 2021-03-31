#include <stdio.h>
#include <string.h>

int main() {
    FILE *fd;
    char line[32], box_ids[250][32];
    int letters[32], count2, count3, total2 = 0, total3 = 0, boxptr = 0;
    int i, j, k;

    if( !(fd = fopen("02-input.txt", "r")) )
        return printf("02-input.txt: cannot open\n"), 1;
    while( fgets(line, 32, fd) ) {
        line[strlen(line)-1] = 0;
        strncpy(box_ids[boxptr++], line, 32);

        count2 = count3 = 0;
        for( i=0; i<26; i++ )
            letters[i] = 0;
        for( i=0; i<strlen(line); i++ )
            letters[line[i] - 97]++;

        for( i=0; i<26; i++ )
            if( letters[i] == 2 )
                count2 = 1;
            else if( letters[i] == 3 )
                count3 = 1;
        total2 += count2;
        total3 += count3;
    }

    printf("%d\n", total2 * total3);
    for( i=0; i<boxptr; i++ )
        for( j=0; j<boxptr; j++ ) {
            int diff;

            if( i == j )
                continue;

            diff = 0;
            for( k=0; k<strlen(box_ids[0]); k++ )
                diff += box_ids[i][k] != box_ids[j][k];
            if( diff == 1 ) {
                for( k=0; k<strlen(box_ids[i]); k++ )
                    if( box_ids[i][k] == box_ids[j][k] )
                        putchar(box_ids[i][k]);
                puts("");
                return 0;
            }
        }
}
