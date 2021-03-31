#include <stdio.h>

struct claim {
    int claim_num;
    int x, y;
    int sx, sy;
};

int main() {
    FILE *fd;
    int plot[1000][1000] = {0};
    struct claim claim_list[1500];
    int cptr = 0, i, j, total = 0;
    char line[40];

    if( !(fd = fopen("03-input.txt", "r")) )
        return printf("03-input: cannot read\n"), 1;
    while( fgets(line, 40, fd) ) {
        int claim_num, x, y, sx, sy;

        sscanf(line, "#%d @ %d,%d: %dx%d\n", &claim_num, &x, &y, &sx, &sy);

        claim_list[cptr].claim_num = claim_num;
        claim_list[cptr].x = x;
        claim_list[cptr].y = y;
        claim_list[cptr].sx = sx;
        claim_list[cptr].sy = sy;
        cptr++;

        for( i=0; i<sx; i++ )
            for( j=0; j<sy; j++ )
                plot[x + i][y + j]++;
    }
    for( i=0; i<1000; i++ )
        for( j=0; j<1000; j++ )
            if( plot[i][j] > 1 )
                total++;
    printf("%d\n", total);

    for( int c=0; c<cptr; c++ ) {
        struct claim clm;
        int multiple;

        multiple = 0;
        clm = claim_list[c];
        for( i=0; i<clm.sx; i++ )
            for( j=0; j<clm.sy; j++ )
                if( plot[clm.x + i][clm.y + j] > 1 )
                    multiple = 1;
        if( !multiple ) {
            printf("%d\n", clm.claim_num);
            return 0;
        }
    }
}
