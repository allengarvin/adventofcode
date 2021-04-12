// use -lbsd 
#include <stdio.h>
#include <sys/types.h>
#include <bsd/md5.h>
#include <string.h>

int main() {
    char key[10], seed[20];
    FILE *fd;
    char passwd1[9] = { 0 } , passwd2[9] = { 0 };
    int pos1 = 0, part2;

    if( !(fd = fopen("05-input.txt", "r")) ) {
        fprintf(stderr, "05-input.txt: unable to open\n");
        return 1;
    }
    fgets(key, 9, fd);

    for( int i=0; ; i++ ) {
        struct MD5Context context;
        unsigned char digest[16];

        snprintf(seed, 20, "%s%d", key, i);
        MD5Init(&context);
        MD5Update(&context, seed, strlen(seed));
        MD5Final(digest, &context);

        if( digest[0] == 0 && digest[1] == 0 && (digest[2]>>4) == 0 ) {
            int c1, c2;

            c1 = digest[2] & 15;
            c2 = digest[3] >> 4;

            if( pos1 < 8 )
                passwd1[pos1++] = (char) (c1 < 10 ? 48 + c1 : 87 + c1);

            if( c1 < 8 && passwd2[c1] == 0 )
                passwd2[c1] = (char) (c2 < 10 ? 48 + c2 : 87 + c2);

            part2 = 1;
            for( int j=0; j<8; j++ )
                part2 &= !!passwd2[j];
            if( part2 )
                break;
                
        }
    }
    printf("%s\n", passwd1);
    printf("%s\n", passwd2);
}

