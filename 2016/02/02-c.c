#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[1024], passcode1[6] = {0}, passcode2[6] = {0};
    int keypad[5][5] = { { 0, 0, 1, 0, 0 },
                         { 0, 2, 3, 4, 0 },
                         { 5, 6, 7, 8, 9 },
                         { 0, 10, 11, 12, 0, },
                         { 0, 0, 13, 0, 0 } };

    int x1 = 1, y1 = 1, x2 = 2, y2 = 2, line = 0;

    fd = fopen(argc == 1 ? "02-input.txt" : argv[1], "r");
    if( !fd ) {
        printf("%s: cannot open\n", argc == 1 ? "02-input.txt" : argv[1]);
        return 1;
    }
    while( fgets(buf, 1023, fd) ) {
        int sx, sy, val;

        buf[strlen(buf)-1] = 0;
        for( int i=0; i<strlen(buf); i++ ) {
            switch( buf[i] ) {
                case 'U': sx = 0; sy = -1; break;
                case 'D': sx = 0; sy =  1; break;
                case 'L': sx = -1; sy = 0; break;
                case 'R': sx =  1; sy = 0; break;
            }
            x1 += 0 <= x1 + sx && x1 + sx <= 2 ? sx : 0;
            y1 += 0 <= y1 + sy && y1 + sy <= 2 ? sy : 0;

            if( y2 + sy >= 0 && y2 + sy <= 4 && x2 + sx >= 0 && x2 + sx <= 4 && 
                keypad[y2 + sy][x2 + sx] ) {
                x2 += sx;
                y2 += sy;
            }
        }
        passcode1[line] = (y1 * 3 + x1) + 49;

        val = keypad[y2][x2];
        passcode2[line++] = val < 10 ? 48 + val : 55 + val;
    }
    printf("%s\n", passcode1);
    printf("%s\n", passcode2);
}


