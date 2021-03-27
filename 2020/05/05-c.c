#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int binary_conversion(char s[]) {
    int n = 0;

    for( int i=0; i<10; i++ )
        n = (n << 1) | (s[i] == 'B' || s[i] == 'R');
    return n;
}
        
int compare(const void *a, const void *b) {
    return *(int *)a > *(int *)b;
}

int main() {
    FILE *fd;
    char bin[13];
    int seats[1024], seat_end = 0;

    if( !(fd = fopen("05-input.txt", "r")) )
        return 1;
    while( fgets(bin, 12, fd) != NULL ) {
        bin[strlen(bin)-1] = '\0';
        seats[seat_end++] = binary_conversion(bin);
    }
    qsort(seats, seat_end, sizeof(int), compare);
    printf("%d\n", seats[seat_end-1]);

    for( int i = 0; i < seat_end; i++ ) 
        if( seats[i] != i + seats[0] ) {
            printf("%d\n", i + seats[0]);
            return 0;
        }
}
