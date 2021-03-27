#include <stdio.h>
#include <string.h>

int traverse(int step[], char map[][33], int max) {
    int x=0, y=0, count=0;
    int side;

    side = (int) strlen(map[0])-1;

    while( y < max ) {
        count += map[y][x] == '#' ? 1 : 0;
        y += step[1];
        x = (x + step[0]) % side;
    }
    return count;
    
}

int main() {
    FILE *fd;
    char map[350][33];
    int max_line = 0;
    int steps[5][2] = { {3,1}, {1,1}, {5,1}, {7,1}, {1,2} };
    long total = 1;

    if( !(fd = fopen("03-input.txt", "r")) ) {
        fprintf(stderr, "03-input.txt: unable to open\n");
        return 1;
    }

    while( fgets(map[max_line++], 33, fd) != NULL )
        ;
    
    for( int i=0; i<5; i++ ) {
        int c;

        c = traverse(steps[i], map, max_line);
        if( i == 0 )
            printf("%d\n", c);
        total *= (long) c;
    }
    printf("%d\n", total);
}
