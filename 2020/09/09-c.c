#include <stdio.h>
#include <stdlib.h>

#define INPUT_SIZE 1000

int part1(long numbers[], int lno) {
    for( int i=lno-25; i<lno; i++ )
        for( int j=i+1; j<lno; j++ )
            if( numbers[lno] - numbers[i] == numbers[j] )
                return 0;

    return 1;
}

long part2(long numbers[], int lno) {
    long total;

    for( int i=0; i<lno; i++ )
        for( int j=i+1; j<lno; j++ ) {
            total = 0;
            for( int k=i; k<=j; k++ )
                total += numbers[k];
            if( total == numbers[lno] ) {
                long min, max;
                min = max = numbers[i];
                for( int k=i; k<=j; k++ ) {
                    min = min < numbers[k] ? min : numbers[k];
                    max = max > numbers[k] ? max : numbers[k];
                }
                return min + max;
            }
        }
    return -1;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    long numbers[INPUT_SIZE];     // size of our input. I assume everyone's is the same?
    int i;

    if( !(fd = fopen(argc == 1 ? "09-input.txt" : argv[1], "r")) ) {
        fprintf(stderr, "%s: unable to open file\n", argc == 1 ? "09-input.txt" : argv[1]);
        return 1;
    }
    for( i=0; i<INPUT_SIZE; i++ )
        fscanf(fd, "%ld\n", &numbers[i]);

    for( i=25; i<INPUT_SIZE; i++ )
        if( part1(numbers, i) ) {
            printf("%ld\n", numbers[i]);
            printf("%ld\n", part2(numbers, i));
            break;
        }
    
}
