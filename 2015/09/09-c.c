#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN(A, B) A < B ? A : B
#define MAX(A, B) A > B ? A : B

// sigh, I guess I have to use a global var
int min_distance = 0x7ffffff, max_distance = -1;

void calculate(int *arr, int sz, int **grid) {
    int distance = 0;

    for( int i=0; i < sz-1; i++ )
        distance += grid[arr[i]][arr[i + 1]];
    min_distance = MIN(min_distance, distance);
    max_distance = MAX(max_distance, distance);
}

void swap(int *arr, int n1, int n2) {
    int tmp;
   
    tmp = arr[n1];
    arr[n1] = arr[n2];
    arr[n2] = tmp;
}

void permute(int *arr, int sz, int n, int **grid) {
    int tmp;
    if( sz == 1 ) {
        calculate(arr, n, grid);
        return;
    }

    for( int i=0; i < sz; i++ ) {
        permute(arr, sz - 1, n, grid);
        
        if( sz % 2 == 1 ) 
            swap(arr, 0, sz-1);
        else
            swap(arr, i, sz-1);
    }
}

void heap_permutation_start(int **grid, int sz) {
    int *arr;

    arr = (int *) malloc(sizeof(int *) * sz);
    for( int i=0; i<sz; i++ )
        arr[i] = i;
    permute(arr, sz, sz, grid);
}

int c_index(char cities[][20], int sz, char *city) {
    for( int i=0; i<sz; i++ )
        if( strcmp(cities[i], city) == 0 )
            return i;
    printf("BUG: c_index of %s not found\n", city);
    exit(1);
}

int **build_grid(char cities[][20], int sz, FILE *fd) {
    int **grid;
    char c1[20], c2[20];
    int d;

    grid = (int **) malloc(sizeof(int *) * sz);
    for( int i=0; i<sz; i++ )
        grid[i] = (int *) malloc(sizeof(int) * sz);

    while( fscanf(fd, "%s to %s = %d\n", &c1, &c2, &d) != EOF ) {
        int i1, i2;
        i1 = c_index(cities, sz, c1);
        i2 = c_index(cities, sz, c2);

        grid[i1][i2] = grid[i2][i1] = d;
        grid[i1][i1] = 0;
        grid[i2][i2] = 0;
    }
    return grid;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char c1[20], c2[20];
    char cities[10][20];
    int **grid;
    int cptr;

    fd = fopen(argc == 1 ? "09-input.txt" : argv[1], "r");
    if( !fd ) {
        fprintf(stderr, "%s: unable to open\n", argc == 1 ? "09-input.txt" : argv[1]);
        return 1;
    }

    while( fscanf(fd, "%s to %s = %*d\n", &c1, &c2) != EOF ) {
        if( cptr == 0 || strcmp(cities[cptr-1], c1) ) {
            strncpy(cities[cptr], c1, strlen(c1) + 1);
            cptr++;
        }
    }

    strncpy(cities[cptr++], c2, strlen(c2)+1);
    fseek(fd, 0, 0);
    grid = build_grid(cities, cptr, fd);
    heap_permutation_start(grid, cptr);

    printf("%d\n%d\n", min_distance, max_distance);
}
