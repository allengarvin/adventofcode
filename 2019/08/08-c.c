#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <unistd.h>

char *read_image() {
    struct stat st;
    int sz;
    char *s;
    FILE *fd;

    stat("08-input.txt", &st);
    sz = st.st_size;
    s = (char *) malloc(sz * (sizeof(char)+1));
    if( !(fd = fopen("08-input.txt", "r")) ) {
        printf("08-input: unable to open\n");
        exit(1);
    }
    fgets(s, sz, fd);
    return s;
}

int least_zeros(char *img) {
    int zeros = 0x7ffffff, layer = -1, j, i, c1 = 0, c2 = 0, zcount;

    for( i=0; i < strlen(img) / (25*6); i++ ) {
        int offset;

        offset = i * (25*6);
        zcount = 0;
        for( j=0; j < 25*6; j++ )
            if( img[i * 25 * 6 + j] == '0' )
                zcount++;
        if( zcount < zeros ) {
            zeros = zcount;
            layer = i;
        }
    }
    for( j=0; j < 25*6; j++ ) {
        char c;

        c = img[layer * 25 * 6 + j]; 
        if( c == '1' )
            c1++;
        else if( c == '2' )
            c2++;
    }
    return c1*c2;
}

int main(int argc, char *argv[]) {
    char *img_s;
    char mesg[6][27] = {0};
    int layers;

    img_s = read_image();

    printf("%d\n", least_zeros(img_s));

    layers = strlen(img_s) / (25*6);
    for( int j=0; j<6; j++ ) {
        for( int i=0; i<25; i++ ) {
            for( int k=0; k<layers; k++ ) {
                char c;
                c = img_s[k * 6 * 25 + j * 25 + i];
                if( c != '2' ) {
                    printf("%c", c == '0' ? ' ' : '#');
                    break;
                }
            }
        }
        puts("");
    }
}
