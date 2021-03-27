#include <stdio.h>

int count(int grid[1000][]) {
    int t = 0;

    for( i=0; i < 1000; i++ )
        for( j=0; j< 1000; j++ )
            t += grid[i][j];
    return t;
}

    
int main() { 
    FILE *fd;
    int grid1[1000][1000] = {0};
    int grid2[1000][1000] = {0};
    char s[81];
    int x1,y1,x2,y2, i, j;

    fd = fopen("06-input.txt", "r");
    if( !fd ) {
        fprintf(stderr, "06-input.txt: unable to read\n");
        return 1;
    }
    while( fgets(s, 80, fd) != NULL ) {
        if( sscanf(s, "turn on %d,%d through %d,%d\n", &x1, &y1, &x2, &y2) ) {
            for( i=x1; i <= x2; i++ )
                for( j=y1; j<= y2; j++ ) {
                    grid1[i][j] = 1;
                    grid2[i][j]++;
                }
        } else if( sscanf(s, "toggle %d,%d through %d,%d\n", &x1, &y1, &x2, &y2) ) {
            for( i=x1; i <= x2; i++ )
                for( j=y1; j<= y2; j++ ) {
                    grid1[i][j] = !grid1[i][j];
                    grid2[i][j] += 2;
                }
        } else if( sscanf(s, "turn off %d,%d through %d,%d\n", &x1, &y1, &x2, &y2) ) {
            for( i=x1; i <= x2; i++ )
                for( j=y1; j<= y2; j++ ) {
                    grid1[i][j] = 0;
                    grid2[i][j] -= grid2[i][j] ? 1 : 0;
                }
        }
    }
    printf("%d\n%d\n", count(grid1), count(grid2);
}
    
