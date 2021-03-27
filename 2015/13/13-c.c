#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Going to reuse a lot of code from day #9, which was an undirected graph, unlike this directed graph

#define MAX(A, B) A > B ? A : B
int max_happiness;

void calculate(int *arr, int sz, int **grid) {
    int happiness = 0;

    for( int i=0; i < sz; i++ )
        happiness += grid[arr[i]][arr[(i + 1) % sz]] + grid[arr[(i + 1) % sz]][arr[i]];

    max_happiness = MAX(happiness, max_happiness);
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

void heap_permutation_start(int **grid, int sz)  {
    int *arr;

    arr = (int *) malloc(sizeof(int *) * sz);
    for( int i=0; i<sz; i++ )
        arr[i] = i;
    permute(arr, sz, sz, grid);

}

int number_of_people(FILE *fd) {
    char line[80], who[30];
    int cnt;

    for( cnt = 0; fgets(line, 80, fd); cnt++ ) {
        line[strcspn(line, " ")] = '\0';
        if( cnt == 0)
            strcpy(who, line);
        else if( strcmp(line, who) )
            break;
    }
    return cnt + 1;
}

// Basically repackaging problem 9
int **build_grid(FILE *fd, int sz) {
    int **grid, happiness, p1, p2;
    char line[80], p1_str[20], p2_str[20];

    grid = (int **) malloc(sizeof(int *) * sz);
    for( int i=0; i<sz; i++ ) {
        grid[i] = (int *) malloc(sizeof(int) * sz);
        for( int j=0; j<sz; j++ )
            grid[i][j] = 0;
    }

    fseek(fd, 0, 0);
    while( fgets(line, 80, fd) ) {
        line[strlen(line)-2] = '\0';
        if( sscanf(line, "%s would gain %d happiness units by sitting next to %s", &p1_str, &happiness, &p2_str) != 3 ) {
            sscanf(line, "%s would lose %d happiness units by sitting next to %sn", &p1_str, &happiness, &p2_str);
            happiness = -happiness;
        }
        
        // Grr, they're in alphabetical order except for Mallory.
        if( p1_str[0] == 'M' ) p1_str[0] = 'H';
        if( p2_str[0] == 'M' ) p2_str[0] = 'H';

        p1 = p1_str[0] - 65;
        p2 = p2_str[0] - 65;
        //printf("%s -> %s: %d %d\n", p1_str, p2_str, p1, p2);
        grid[p1][p2] = happiness;

    }
    return grid;
}

int main() {
    FILE *fd;
    int pcnt;
    int **grid;

    fd = fopen("13-input.txt", "r");
    if( !fd )
        return fprintf(stderr, "13-input.txt: unable to read"), 1; 

    pcnt = number_of_people(fd);
    grid = build_grid(fd, pcnt + 1);

    max_happiness = 0;
    heap_permutation_start( grid, pcnt ); 
    printf("%d\n", max_happiness);
    max_happiness = 0;
    heap_permutation_start( grid, pcnt+1 ); 
    printf("%d\n", max_happiness);

}
