#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int captcha(char *a, int offset) {
    int sum = 0;
    for( int i=0; i<strlen(a); i++ )
        if( a[i] == a[(i + offset) % strlen(a)] )
            sum += (int) a[i] - 48;
    return sum;
}

int main() {
    char *a;
    struct stat buf;
    FILE *fd;
    
    if( !(fd = fopen("01-input.txt", "r")) || stat("01-input.txt", &buf) ) {
        fprintf(stderr, "No input file");
        return 1;
    }
    a = (char *) malloc( buf.st_size * sizeof(char));
    fread(a, buf.st_size, 1, fd);
    a[strlen(a)-1] = 0;
    printf("%d\n", captcha(a, 1));
    printf("%d\n", captcha(a, strlen(a) / 2));
}
    

    
