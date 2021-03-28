#include <stdio.h>

int fuel(int m, int recurp) {
   int f;

    f = m / 3 - 2;
    if( f <= 0 )
        return 0;
    if( !recurp )
        return f;
    return f + fuel(f, 1); 
}

int main() {
    FILE *fd;
    int total1 = 0, total2 = 0;
    int mass;
    
    fd = fopen("01-input.txt", "r");
    while( fscanf(fd, "%d", &mass) != EOF ) {
        total1 += fuel(mass, 0);
        total2 += fuel(mass, 1);
    }
    printf("%d\n", total1);
    printf("%d\n", total2);
}
