#include <stdio.h>
#include <stdlib.h>

struct node {
    int x, y, step, i;
    struct node *next;
    int complete;
};

struct node *head, *last;
int offset;

struct node *add_node(int x, int y, int step) {
    struct node *n, *l;
    int i = 0;

    for( n = head; n; n = n->next ) {
        if( n->x == x && n->y == y )
            return NULL;
        l = n;
        i++;
    }

    n = (struct node *) malloc(sizeof(struct node));
    n->x = x;
    n->y = y;
    n->complete = 0;
    n->next = NULL;
    n->step = step;
    n->i = i;
    l->next = n;
    last = n;

    return n;
}

int openp(int x, int y) {
    int i, cnt;

    if( x == 0 && y == 0 )
        return 1;

    if( x < 0 || y < 0 )
        return 0;

    i = x * x + 3 * x + 2 * x * y + y + y * y + offset;
    for( cnt = 0; i != 1; i /= 2 )
        cnt += i % 2;
    cnt += i % 2;

    return !(cnt % 2);
}

int containp(int x, int y) {
    struct node *n;

    for( n=head; n; n = n->next ) {
        if( n->x == x && n->y == y ) {
            return 1;
        }
    }
    return 0;
}

void flood(struct node *n, int step) {
    int i, j;

    i = n->x;
    j = n->y;

    if( openp(i-1, j) && !containp(i-1, j) ) add_node(i-1, j, step);
    if( openp(i+1, j) && !containp(i+1, j) ) add_node(i+1, j, step);
    if( openp(i, j-1) && !containp(i, j-1) ) add_node(i, j-1, step);
    if( openp(i, j+1) && !containp(i, j+1) ) add_node(i, j+1, step);
    n->complete = 1;
}

void run_step(int step) {
    struct node *n, *l;

    l = last;
    for( n = head; n && n->step <= step; n = n->next ) {
        if( !n->complete )
            flood(n, step+1);
    }
    //printf("Step: %d Size: %d\n", step, last->i);
}

int main() {
    FILE *fd;
    int i, part2;

    if( !(fd = fopen("13-input.txt", "r")) )
        return printf("13-input.txt: cannot open\n"), 1;
    fscanf(fd, "%d\n", &offset);

/*
    for( int j=0; j<50; j++ ) {
        for( int i=0; i<80; i++ )
            printf("%c", openp(i, j) ? (i == 31 && j == 39 ? '@' : '.') : '#');
        puts("");
    }
    return 0;
*/

    head = (struct node *) malloc(sizeof(struct node));
    head->x = 0;
    head->y = 0;
    head->step = 0;
    head->complete = 0;
    head->next = NULL;

    last = head;

    for( i=0; !containp(31, 39); i++ ) {
        run_step(i);
        //printf("%d\n", i);
        if( i == 51 )
            part2 = last->i;
    }
    printf("%d\n", i-2);
    printf("%d\n", part2);
}
