#include <stdio.h>

#define SWAP(A,B) { A ^= B; B ^= A; A ^= B; }

void sort3(int a[3]) {
    if( a[0] > a[1] )
        SWAP(a[0], a[1])
    if( a[1] > a[2] )
        SWAP(a[1], a[2])
    if( a[0] > a[1] )
        SWAP(a[0], a[1])
}

int paper(int arr[3]) {
    return 2 * (arr[0] * arr[1] + arr[0] * arr[2] + arr[1] * arr[2]) + arr[0] * arr[1];
}

int ribbon(int arr[3]) {
    return 2 * (arr[0] + arr[1]) + arr[0] * arr[1] * arr[2];
}

int main() {
    FILE *fd;
    int dimensions[3];
    int p_area = 0, p_ribbon = 0;

    if( !(fd = fopen("02-input.txt", "r")) ) {
        fprintf(stderr, "02-input.txt: unable to open\n");
        return 1;
    }

    while( fscanf(fd, "%dx%dx%d\n", &dimensions[0], &dimensions[1], &dimensions[2]) != EOF ) {
        sort3(dimensions);
        p_area += paper(dimensions);
        p_ribbon += ribbon(dimensions);
    }
    printf("%d\n%d\n", p_area, p_ribbon);
}
