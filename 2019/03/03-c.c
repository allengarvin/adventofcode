#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRIM(s) s[strlen(s)-1] = 0
#define TAXI(s) (abs(s->x) + abs(s->y))

typedef struct node {
    int x, y, steps;
    struct node *next;
} llist;

struct node *follow_path(char *input) {
    llist *head, *next, *prev;
    char *tok;
    int stepx, stepy, steps;

    head = (llist *) malloc(sizeof(llist));
    head->x = 0;
    head->y = 0;
    head->steps = 0;
    head->next = NULL;

    prev = head;

    TRIM(input);

    for( tok = strtok(input, ","); tok != NULL; tok = strtok(NULL, ",") ) {
        switch( tok[0] ) {
            case 'U': stepx = 0; stepy = -1; break;
            case 'D': stepx = 0; stepy = 1; break;
            case 'L': stepx = -1; stepy = 0; break;
            case 'R': stepx = 1; stepy = 0; break;
        }
        steps = atoi(tok+1);
        next = (llist *) malloc(sizeof(llist));

        prev->next = next;
        next->x = prev->x + stepx * steps;
        next->y = prev->y + stepy * steps;
        next->steps = steps;
        next->next = NULL;

        prev = next;

    }
    return head;
}

// From https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
int ccw(int ax, int ay, int bx, int by, int cx, int cy) {
    return ((cy - ay) * (bx - ax)) > ((by - ay) * (cx - ax));
}

llist *intersect(int ax, int ay, int bx, int by, int cx, int cy, int dx, int dy) {
    int step1x, step1y, step2x, step2y, oax, oay, ocx, ocy;
    llist *tmp;

    if( ccw(ax, ay, cx, cy, dx, dy) != ccw(bx, by, cx, cy, dx, dy) &&
           ccw(ax, ay, bx, by, cx, cy) != ccw(ax, ay, bx, by, dx, dy) ) {
        step1x = bx - ax; if( step1x != 0 ) step1x /= abs(step1x);
        step1y = by - ay; if( step1y != 0 ) step1y /= abs(step1y);

        step2x = dx - cx; if( step2x != 0 ) step2x /= abs(step2x);
        step2y = dy - cy; if( step2y != 0 ) step2y /= abs(step2y);

        oax = ax; oay = ay; ocx = cx; ocy = cy;

        for( ax = oax, ay = oay; !(ax == bx && ay == by); ax += step1x, ay += step1y ) {
            if( ax == cx || ay == cy ) {
                //printf("INTERSECTION: (%d,%d)\n", ax, ay);
                tmp = (llist *) malloc(sizeof(llist));
                tmp->x = ax;
                tmp->y = ay;
                return tmp;
            }
        }
        printf("BUG SHOULD NOT REACH\n");
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    char buf[4096];
    llist *path1, *path2, *p1, *p2, *prev1, *prev2, *tmp;
    int minimum = 0x7fffffff, minsteps = 0x7fffffff, steps1 = 0, steps2 = 0;

    fd = fopen(argc == 1 ? "03-input.txt" : argv[1], "r");
    if( !fd )
        printf("No input file\n"), 1;

    path1 = follow_path(fgets(buf, 4095, fd));
    path2 = follow_path(fgets(buf, 4095, fd));

    for( prev1 = path1, p1 = path1->next; p1; prev1 = p1, p1 = p1->next ) {
        steps2 = 0;
        for( prev2 = path2, p2 = path2->next; p2; prev2 = p2, p2 = p2->next ) {
            if( tmp = intersect(prev1->x, prev1->y, p1->x, p1->y, prev2->x, prev2->y, p2->x, p2->y) ) {
                int s1, s2;

                if( TAXI(tmp) < minimum ) 
                    minimum = TAXI(tmp);
                s1 = steps1 + abs(tmp->x - prev1->x) + abs(tmp->y - prev1->y);
                s2 = steps2 + abs(tmp->x - prev2->x) + abs(tmp->y - prev2->y);
                if( s1 + s2 < minsteps )
                    minsteps = s1 + s2;

            }
            steps2 += p2->steps;
        }
        steps1 += p1->steps;
    }
    printf("%d\n", minimum);
    printf("%d\n", minsteps);
}
