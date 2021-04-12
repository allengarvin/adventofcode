#include <stdio.h>

int valid(int a, int b, int c) {
    return a + b > c && a + c > b && b + c > a;
}

int main() {
    FILE *fd;
    int a, b, c, p1[3], p2[3], i, cnt1=0, cnt2=0;

    fd = fopen("03-input.txt", "r");
    if( !fd )
        return printf("03-input.txt: unable to open\n"), 1;

    for( i=0; fscanf(fd, "%d %d %d\n", &a, &b, &c) != EOF; i++ ) {
        switch( (i+1) % 3 ) {
            case 1:
                p1[0] = a;
                p1[1] = b;
                p1[2] = c;
                break;
            case 2:
                p2[0] = a;
                p2[1] = b;
                p2[2] = c;
                break;
            case 0:
                cnt2 += valid(p1[0], p2[0], a) + valid(p1[1], p2[1], b) +valid(p1[2], p2[2], c);
                break;
        }
        cnt1 += valid(a, b, c);
    }
    printf("%d\n%d\n", cnt1, cnt2);
}
