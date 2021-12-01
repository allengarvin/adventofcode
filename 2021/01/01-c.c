#include <stdio.h>
#include <string.h>
#include <errno.h>

#define ARRSZ 2000

int count_ascending(int arr[], int sz) {
    int c = 0;

    for( int i=1; i<sz; i++ )
        if( arr[i] > arr[i-1] )
            c++;
    return c;
}
        
int main(int argc, char *argv[]) {
    FILE *fd;
    int n = 0, arr[ARRSZ];
    int cnt1 = 0, cnt2 = 0;

    if( argc != 2 ) {
        printf("Usage: %s [file]\n", argv[0]);
        return 1;
    }
    if( (fd = fopen(argv[1], "r")) == NULL ) {
        fprintf(stderr, "%s: %d (%s)\n", argv[1], errno, strerror(errno));
        return 1;
    }
    while( (fscanf(fd, "%d\n", &arr[n]) == 1) && n < ARRSZ  )
        n++;

    if( n > ARRSZ ) {
        fprintf(stderr, "%s: max arr length exceeded", argv[1]);
        return 1;
    }
    printf("%d\n", count_ascending(arr, n));
    for( int i=0; i < n - 2; i++ )
        arr[i] = arr[i] + arr[i+1] + arr[i+2];
    printf("%d\n", count_ascending(arr, n-3));
}
