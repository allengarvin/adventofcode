#include <stdio.h>
#include <stdlib.h>

struct node {
    int val;

    struct node *prv, *nxt;
};

struct node *current;

struct node *create_node(int val) {
    struct node *n;

    n = (struct node *) malloc(sizeof(struct node *));
    n->val = val;
    return n;
}

void move_node(int n) {
    for( int i=0; i<abs(n); i++ )
        current = n < 0 ? current->prv : current->nxt;
}

void insert_node(int val) {
    struct node *n, *new;

    n = current;
    
    new = create_node(val);
    new->prv = current;
    new->nxt = current->nxt;

    new->nxt->prv = new;
    new->prv->nxt = new;

    current = new;
}

unsigned int pop() {
    struct node *n;
    int val;

    n = current;

    n->prv->nxt = n->nxt;
    n->nxt->prv = n->prv;

    val = n->val;
    current = n->nxt;
    
    free(n);
    return (unsigned int) val;
}

unsigned int run_game(int pl, int high) {
    unsigned int *scores, max = 0;
    int i, player;
    struct node *zero, *n, *m;

    scores = (unsigned int *) malloc(pl * sizeof(unsigned int));
    for( i=0; i<pl; i++ )
        scores[i] = 0;

    zero = create_node(0);
    zero->prv = zero;
    zero->nxt = zero;
    current = zero;

    for( i=0; i<high; i++ ) {
        player = i % pl;

        if( (i+1) % 23 == 0 ) {
            move_node(-7);
            scores[player] += (unsigned int) i + pop() + 1;
        } else {
            move_node(1);
            insert_node(i+1);
        }
    }
    for( i=0; i<pl; i++ )
        if( max < scores[i] )
            max = scores[i];

    
    for( n = zero->nxt, m = zero->nxt->nxt; m != zero; n = m ) {
        m = n->nxt;
        free(n);
    }
    free(zero);
    return max;
}

int main(int argc, char *argv[]) {
    FILE *fd;
    int players, high_marble;

    if( !(fd = fopen(argc == 1 ? "09-input.txt" : argv[1], "r")) )
        return printf("09-input: cannot open\n"), 1;

    fscanf(fd, "%d players; last marble is worth %d points", &players, &high_marble);
    printf("%u\n", run_game(players, high_marble));
    printf("%u\n", run_game(players, high_marble*100));
}
    
