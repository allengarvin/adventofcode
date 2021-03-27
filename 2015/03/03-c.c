#include <stdio.h>
#include <stdlib.h>

struct Node {
    int x, y;
    struct Node *next;
};

struct Node *mknode(int x, int y) {
    struct Node *n;

    n = (struct Node *) malloc(sizeof(struct Node));
    n->x = x;
    n->y = y;
    n->next = NULL; 
    return n;
}

int find(struct Node *n, int x, int y) {
    while( n != NULL ) {
        if( n->x == x && n->y == y )
            return 1;
        n = n->next;
    }
    return 0;
}

void clear_list(struct Node *n) {
    struct Node *m;

    while( n ) {
        m = n->next;
        free(n);
        n = m;
    }
}

int count(struct Node *n) {
    int i = 0;

    do {
        i++;
        n = n->next;
    } while( n );
    return i;
}

int main() {
    FILE *fd;
    struct Node *first, *last, *n;
    int sx=0, sy=0, rx=0, ry=0, turn=0;
    char c;

    fd = fopen("03-input.txt", "r");
    if( !fd )
        return 1;

    first = last = mknode(sx, sy);
    while( (c = fgetc(fd)) != '\n' ) {
        switch( c ) {
            case '^': sy--; break;
            case 'v': sy++; break;
            case '<': sx--; break;
            case '>': sx++; break;
        }
        if( !find(first, sx, sy) ) {
            n = mknode(sx, sy);
            last->next = n;
            last = n;
        }
        turn++;
    }
    printf("%d\n", count(first));
    clear_list(first);

    sx=0; sy=0;
    first = last = mknode(sx, sx);
    fseek(fd, 0, SEEK_SET);
    turn = 0;
    while( (c = fgetc(fd)) != '\n' ) {
        switch( c ) {
            case '^': turn % 2 ? ry-- : sy--; break;
            case 'v': turn % 2 ? ry++ : sy++; break;
            case '<': turn % 2 ? rx-- : sx--; break;
            case '>': turn % 2 ? rx++ : sx++; break;
        }
        if( turn % 2 ) {
            if( !find(first, rx, ry) ) {
                n = mknode(rx, ry);
                last->next = n;
                last = n;
            }
        } else {
            if( !find(first, sx, sy) ) {
                n = mknode(sx, sy);
                last->next = n;
                last = n;
            }
        }
        turn++;
    }
    printf("%d\n", count(first));
}
    
