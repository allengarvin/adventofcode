#include <ctype.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct tile_obj {
    int id;
    long tile_c;        // long needs to be 64 bit, so on a 32-bit cpu this would fail
    int sides[4], rsides[4];
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

void read_tiles(FILE *fd, Tile *tiles[]) {
    int i, y, x, data;

    for( i=0; i<144; i++ ) {
        Tile *t;
        int tile_n, tmp, top, left, right, bottom;

        t = (Tile *) malloc(sizeof(Tile));
        tiles[i] = t;

        fscanf(fd, "Tile %d:\n", &tile_n);
        t->id = tile_n;
        printf("Reading tile %d\n", t->id);

        top = left = right = bottom = 0;
        data = 0;

        for( y=0; y<10; y++ ) {
            for( x=0; x<10; x++ ) {
                tmp = 0;
                tmp = fgetc(fd) == '#' ? 1 : 0;

                if( x == 0 )
                    left |= tmp << (10-y);
                if( x == 9 )
                    right |= tmp << y;
                if( y == 0 )
                    top |= tmp << x;
                if( y == 9 )
                    bottom |= tmp << (10-x);
                if( x >= 1 && x <= 8 && y >= 1 && y <= 8 ) {
                    data |= tmp;
                    if( x != 8 && y != 8 )
                        data <<= 1;
                }
            }
            fgetc(fd);      // toss newline
        }
        fgetc(fd);      // toss newline
    
        printf("%d,%d,%d,%d\n", top, right, bottom, left);
        printf("%ld\n", data);
    }
}

int main(int argc, char *argv[]) {
    FILE *fd;
    Tile *tiles[144];

    fd = get_file_descriptor(argc, argv);
    read_tiles(fd, tiles);
    
}
