/* Working on this now and then, as it's likely the hardest (as in: tedious) of the 2020 in C */
/* Part1 finished! */
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

#define CORNER 1
#define EDGE 2
#define INNER 3
typedef struct tile_obj {
    int id;
    ulong data;        // long needs to be 64 bit, so on a 32-bit cpu this would fail
    int sides[4];
    int all_sides[8];
    int type;
} Tile;

// Correct 2020-04-28
int reverse(int n) {
    int rev;

    rev = 0;
    for( int i=0; i<10; i++ )
        rev |= !!(n & (1 << (9-i))) << i;
    return rev;
}

void display_border(Tile *t) {
    printf("Border %d:\n", t->id);
    for( int i=0; i<10; i++ )
        putchar(t->sides[0] & (1<<i) ? '#' : '.');
    putchar(10);

    for( int y=0; y<8; y++ ) {
        putchar(t->sides[3] & (1 << (8-y)) ? '#' : '.');
        for( int x=0; x<8; x++ )
            putchar(' ');
        putchar(t->sides[1] & (1 << (y+1)) ? '#' : '.');
        putchar(10);
    }

    for( int i=9; i >= 0; --i )
        putchar((t->sides[2] & (1<<i)) ? '#' : '.');
    putchar(10);
}

// Correct 2020-04-27
void display_tile(Tile *t, int with_borders) {
    ulong d;

    d = t->data;
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

// will check when rotation is in place
void rotate_border(Tile *t, int n) {
    int i;

/*
    printf("sides = {");
    for( i=0; i<4; i++ )
        printf("%5d, ", t->sides[i]);
    printf("}\n");
*/

    for( i=0; i<n; i++ ) {
        int j, last;

        last = t->sides[3];
        for( j=3; j>0; --j )
            t->sides[j] = t->sides[j-1];

        t->sides[0] = last;
    }
/*
    printf("sides = {");
    for( i=0; i<4; i++ )
        printf("%5d, ", t->sides[i]);
    printf("}\n");
*/
}

// Correct: 2020-04-28
void flip_horizontal(Tile *t) {
    ulong new_data;
    int tmp;

    new_data = 0;

    for( int y=0; y<8; ++y )
        for( int x=0; x<8; ++x )
            new_data |= (ulong) !!(t->data & ((ulong) 1 << y * 8 + (7-x))) << (y*8 + x);
    t->data = new_data;

    tmp = t->sides[1];
    t->sides[1] = reverse(t->sides[3]);
    t->sides[3] = reverse(tmp);
    t->sides[0] = reverse(t->sides[0]);
    t->sides[2] = reverse(t->sides[2]);
}

// Correct: 2020-04-28
void flip_vertical(Tile *t) {
    ulong new_data;
    int tmp;

    new_data = 0;
    for( int y=0; y<8; ++y )
        for( int x=0; x<8; ++x )
            new_data |= (ulong) !!(t->data & ((ulong) 1 << ((7-y) * 8 + x))) << (y*8 + x);
    t->data = new_data;

    tmp = t->sides[0];
    t->sides[0] = reverse(t->sides[2]);
    t->sides[2] = reverse(tmp);
    t->sides[1] = reverse(t->sides[1]);
    t->sides[3] = reverse(t->sides[3]);
}

// Correct: 2020-04-28
void rotate90(Tile *t) {
    ulong new_data;

    new_data = (ulong) 0;
    for( int y=0; y<8; y++ )
        for( int x=0; x<8; x++ )
            new_data |= (ulong) !!(t->data & ((ulong) 1 << (y*8+x))) << (ulong) (x * 8 + (7-y));
    t->data = new_data;

    rotate_border(t, 1);
}

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

        t->all_sides[0] = top;
        t->all_sides[1] = right;
        t->all_sides[2] = bottom;
        t->all_sides[3] = left;
        t->all_sides[4] = reverse(top);
        t->all_sides[5] = reverse(right);
        t->all_sides[6] = reverse(bottom);
        t->all_sides[7] = reverse(left);
        t->data = data;

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

/* There are 144*8 = 1152 possible edges
   For a 12x12 grid, there are 2 * 12 * 11 = 264 inner edges--so there should be 264 equal pairs of edges (528 numbers)
   And in fact, printf each side on from all_sides each on a row:
    ./a.out  | sort | uniq -c | grep '^ *2' | wc
    528    1056    6286

    Since we know this is exact, the tile layout was nicely designed for us.
    There are 4 corners, which have only 2 sides in common with other tiles
    There are 40 additional sides, which have 3 sides in common with other tiles
    There are 100 interior sides, which have 4 sides in common
    
    Yay, tests match up exactly! Model is correct
*/

void quick_process(Tile *tiles[]) {
    int cnt, flag;
    Tile *a, *b;

    for( int i=0; i<144; i++ ) {
        cnt = 0;
        a = tiles[i];

        for( int j=0; j<144; j++ ) {

            b = tiles[j];
            if( i == j )
                continue;

            flag = 0;
            for( int x=0; x<8; x++ )
                for( int y=0; y<8; y++ ) {
                    if( a->all_sides[x] == b->all_sides[y] )
                        cnt++;
                }
                    
        }
        if( cnt == 4 ) {
            //printf("Tile %d: corner\n", a->id, cnt);
            a->type = CORNER;
            /*
            printf("  Sides: { ");
            for( int x=0; x<8; x++ ) {
                flag = 0;
                for( int d=0; d<144; d++ ) {
                    if( d == i ) continue;
                    for( int e=0; e<8; e++ ) {
                        if( a->all_sides[x] == tiles[d]->all_sides[e] ) {
                            printf("*%d*, ", a->all_sides[x]);
                            flag = 1;
                            break;
                        }
                        if( flag ) break;
                    }
                    if( flag ) break;
                }
                if( !flag )
                    printf("%d, ", a->all_sides[x]);
            }
            printf("}\n"); */
        }
        if( cnt == 6 ) {
            //printf("Tile %d: edge\n", a->id, cnt);
            a->type = EDGE;
        }
        if( cnt == 8 ) {
            //printf("Tile %d: interior\n", a->id, cnt);
            a->type = INNER;
        }
    }
}

int valid_side(Tile *tiles[], int t_indx, int side) {
    for( int i=0; i<144; i++ ) {
        if( i == t_indx )
            continue;
        for( int j=0; j<8; j++ )
            if( tiles[i]->all_sides[j] == tiles[t_indx]->sides[side] )
                return 1;
    }
}

Tile *choose_topleft_corner(Tile *tiles[]) {
    Tile *t;
    int side;

    for( int i=0; i<144; i++ ) {
        t = tiles[i];

        if( t->type == CORNER ) { //placeholder. Eventually I want to choose a particular tile that lines up the monsters nicely
            // Let's rotate it so the right and bottom are the sides (sides[1] && sides[2])

            for( int side=0; side<4; side++ ) {
                if( valid_side(tiles, i, side) && valid_side(tiles, i, (side+1)%4) ) {
                    if( side == 0 )
                        rotate90(t);
                    if( side == 2 ) {
                        rotate90(t);
                        rotate90(t);
                        rotate90(t);
                    }
                    if( side == 3 ) {
                        rotate90(t);
                        rotate90(t);
                    }
                    break;
                }
            }
            return t;
        }
    }
}

Tile *choose_right(Tile *tiles[], Tile *t) {
    int j;
    for( int i=0; i<144; i++ ) {
        if( tiles[i]->id == t->id )
            continue;
        for( int j=0; j<8; j++ ) {
            if( tiles[i]->all_sides[j] == reverse(t->sides[1]) ) { // think I need to check reverse
                printf("FOUND RIGHT for tile %d (%d)\n", t->id, j);
                exit(1);
                return tiles[i];
            }
        }
        if( j == 8 ) {
            printf("BUG! choose-right\n");
            exit(1);
        }
    }
}

Tile *choose_down(Tile *tiles[], Tile *t) {
    int j;
}

int solve_puzzle(Tile *tiles[]) {
    Tile *corner, *t, *left;
    int i;

    corner = choose_topleft_corner(tiles);
    left = corner;
    for( int y=0; y<12; y++ ) {
        t = left;
        for( int x=0; x<12; x++ ) {
            t = choose_right(tiles, t);
        }
        left = choose_down(tiles, left);
    }
        
}

int main(int argc, char *argv[]) {
    FILE *fd;
    Tile *tiles[144];
    ulong total;

    fd = get_file_descriptor(argc, argv);
    read_tiles(fd, tiles);
/*    for( int i=0; i<144; i++ ) {
        for( int j=0; j<8; j++ )
            printf("%d\n", tiles[i]->all_sides[j]);
    } */
    quick_process(tiles);
    
    total = (ulong) 1;
    for( int i=0; i<144; i++ )
        if( tiles[i]->type == CORNER ) {
            total *= (ulong) tiles[i]->id;
        }
    printf("%lu\n", total);
    solve_puzzle(tiles);
}
