// use -lbsd 
#include <stdio.h>
#include <sys/types.h>
#include <bsd/md5.h>
#include <string.h>

int main() {
    char key[10], seed[20];
    FILE *fd;
    int part1 = 0, part2 = 0;

    if( !(fd = fopen("04-input.txt", "r")) ) {
        fprintf(stderr, "04-input.txt: unable to open\n");
        return 1;
    }
    fgets(key, 9, fd);
    for( int i = 254575; ; i++ ) {
        struct MD5Context context;
        unsigned char digest[16];

        snprintf(seed, 20, "%s%d", key, i);
        MD5Init(&context);
        MD5Update(&context, seed, strlen(seed));
        MD5Final(digest, &context);

        if( digest[0] == 0 && digest[1] == 0 && digest[2] == 0 && !part2 )
            part2 = i;
        if( digest[0] == 0 && digest[1] == 0 && (digest[2] >> 8) == 0 && !part1 )
            part1 = i;

        if( part1 && part2 )
            break;
    }
    printf("%d\n%d\n", part1, part2);
}

