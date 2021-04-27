/* Working on this now and then, as it's likely the hardest (as in: tedious) of the 2020 in C */
#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Todo:
    flip horizontally, flip vertically, switching the data and the sides appropriately
    rotate 90: should be easy on the sides, just an array rotate
               for data, use: https://stackoverflow.com/questions/6930667/what-is-the-fastest-way-to-transpose-the-bits-in-an-8x8-block-on-bits
            (should be in Hacker's Delight, if I can find my copy)

    Then, we find 4 corners and built left-to-right
    Then, stitch together puzzle pieces and pick out the serpents
*/
typedef struct tile_obj {
    int id;
    ulong tile_c;        // long needs to be 64 bit, so on a 32-bit cpu this would fail
    int sides[4];
} Tile;

FILE *get_file_descriptor(int argc, char *argv[]) {
    FILE *fd;
    char *fn;

    if( argc > 1 )
        fn = argv[1];
    else {
        fn = (char *) malloc(13);
        strncat(fn+2, "-input.txt", 12);

        if( isdigit(argv[0][0]) && isdigit(argv[0][1]) && argv[0][2] == '-' ) {
            fn[0] = argv[0][0];
            fn[1] = argv[0][2];
        } else {
            char *buf;
            int i;

            buf = (char *) malloc(80);
            getcwd(buf, 79);
            
            for( i=strlen(buf); i; i-- )
                if( buf[i] == '/' )
                    break;

            if( isdigit(buf[i+1]) && isdigit(buf[i+2]) ) {
                fn[0] = buf[i+1];
                fn[1] = buf[i+2];
            } else {
                fprintf(stderr, "%s: unable to determine input filename from executable or PWD\n", argv[0]);
                exit(EXIT_FAILURE);
            }
            free(buf);
        }
    }
    fd = fopen(fn, "r");
    if( !fd ) {
        fprintf(stderr, "%s: %s\n", fn, strerror(errno));
        exit(EXIT_FAILURE);
    }
    return fd;
}

int reverse(int n) {
    int rev;

    rev = 0;
    while( n > 0 ) {
        rev <<= 1;
        if( n & 1 )
            rev ^= 1;
        n >>= 1;
    }
    return rev;
}

// Correct 2020-04-27
void display_tile(Tile *t, int with_borders) {
    ulong d;

    d = t-> tile_c;
    printf("Tile %d:\n", t->id);
    if( with_borders ) {
        for( int i=0; i<10; i++ )
            putchar(t->sides[0] & (1<<i) ? '#' : '.');
        putchar(10);
    }

    for( int y=0; y<8; y++ ) {
        if( with_borders ) {
            putchar(t->sides[3] & (1 << (8-y)) ? '#' : '.');
        }
        for( int x=0; x<8; x++ )
            putchar(d & ((ulong) 1 << (ulong) y*8 + x) ? '#' : '.');
        if( with_borders ) {
            putchar(t->sides[1] & (1 << (y+1)) ? '#' : '.');
        }
        putchar(10);
    }

    if( with_borders ) {
        for( int i=9; i >= 0; --i )
            putchar((t->sides[2] & (1<<i)) ? '#' : '.');
        putchar(10);
    }
}

// Correct 2020-04-27
void read_tiles(FILE *fd, Tile *tiles[]) {
    int i, y, x;
    ulong data;

    for( i=0; i<144; i++ ) {
        Tile *t;
        int tile_n, tmp, top, left, right, bottom;

        t = (Tile *) malloc(sizeof(Tile));
        tiles[i] = t;

        fscanf(fd, "Tile %d:\n", &tile_n);
        t->id = tile_n;
        //printf("Reading tile %d\n", t->id);

        top = left = right = bottom = 0;
        data = (ulong) 0;

        for( y=0; y<10; y++ ) {
            for( x=0; x<10; x++ ) {
                tmp = 0;
                tmp = fgetc(fd) == '#' ? 1 : 0;

                if( x == 0 )
                    left |= tmp << (9-y);
                if( x == 9 )
                    right |= tmp << y;
                if( y == 0 )
                    top |= tmp << x;
                if( y == 9 )
                    bottom |= tmp << (9-x);
                if( x >= 1 && x <= 8 && y >= 1 && y <= 8 ) {
                    data |= (ulong) tmp << (ulong) ((y-1)*8 + (x-1));
                }
            }
            fgetc(fd);      // toss newline
        }
        fgetc(fd);      // toss newline
        t->sides[0] = top;
        t->sides[1] = right;
        t->sides[2] = bottom;
        t->sides[3] = left;

        t->tile_c = data;

        if( i == 0 && 0 ) {    
            /*
                Tile 1319:
                #.########
                ##.#.#.#..
                .....#..##
                .#.....#..
                .........#
                #.........
                #..##...#.
                #.#.#...##
                .#....#...
                ....##..#.

            //  def conv(s): return int(s.replace(".", "0").replace("#", "1"), 2)
                top:
                >>> conv('#.########')
                767
                >>> conv('#.########'[::-1])
                1021
                
                right:
                >>> conv('#.#.#..#..')
                676
                >>> conv('#.#.#..#..'[::-1])
                149
                
                bottom: 
                >>> conv('.#..##....')
                304
                >>> conv('.#..##....'[::-1])
                50
                
                left:
                >>> conv('..###...##')
                227
                >>> conv('..###...##'[::-1])
                796
            */
            //Reading tile 1319
            //top=1021,right=149,bottom=50,left=796

            //top=1021,right=149,bottom=50,left=796
            //rtop=767,rright=169,rbottom=19,rleft=227 // Currently wrong *******


            if( top != 1021 ) {
                printf("Top incorrect\n"); exit(1);
            }
            printf("top=%d,right=%d,bottom=%d,left=%d\n", top, right, bottom, left);
            printf("rtop=%d,rright=%d,rbottom=%d,rleft=%d\n", reverse(top), reverse(right), reverse(bottom), reverse(left));
            /*
                >>> conv('#.#.#.#.....#..##.....#...................##...#.#.#...##....#..'[::-1])
                2416898081669877845
                >>> conv('#.#.#.#.....#..##.....#...................##...#.#.#...##....#..')
                12252467197752988036
                >>> math.log2(2416898081669877845)
                61.06786234525905
                >>> math.log2(12252467197752988036)
                63.40970608723641
                >>> 
            */

            //display_tile(t, 0);
            display_tile(t, 1);
            return;
        }
        /*
        agarvin@atg-home:~/programming/adventofcode/2020/20$ ./a.out  > 2
        agarvin@atg-home:~/programming/adventofcode/2020/20$ diff 20-input.txt 2
        agarvin@atg-home:~/programming/adventofcode/2020/20$ !v
        display_tile(t, 1);
        putchar(10);
        */
    }
}

int main(int argc, char *argv[]) {
    FILE *fd;
    Tile *tiles[144];

    fd = get_file_descriptor(argc, argv);
    read_tiles(fd, tiles);
    
}
