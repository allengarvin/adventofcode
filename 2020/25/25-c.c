#include <stdio.h>
#include <stdlib.h>

struct transformation {
    int cnt;
    int key;
};

struct transformation *transform(int subject, int key1, int key2, int setloops) {
    struct transformation *t;
    int val = 1, cnt = 1;

    t = (struct transformation *) malloc(sizeof(struct transformation));
    for( cnt=1; ; ++cnt ) {
        val = ((long) val * (long) subject) % 20201227;

        if( key1 > -1 ) {
            if( val == key1 ) {
                t->cnt = cnt;
                t->key = key2;
                return t;
            } else if( val == key2 ) {
                t->cnt = cnt;
                t->key = key1;
                return t;
            }
        } else if( cnt == setloops ) {
            t->key = val;
            return t;
        }
    }
}


int main(void) {
    int key1, key2;
    struct transformation *t;
    FILE *fd;

    if( !(fd = fopen("25-input.txt", "r")) )
        return puts("25-input: unable to open\n"), 1;

    fscanf(fd, "%d\n", &key1);
    fscanf(fd, "%d\n", &key2);

    t = transform(7, key1, key2, 0);
    t = transform(t->key, -1, -1, t->cnt);
    printf("%d\n", t->key);
}
