#include <stdio.h>
#include <stdlib.h>

#define MOD(a, b) ((a % b) + b) % b
struct movement {
    char a;
    int b;
};

int part1(struct movement *m, int sz) {
    int x = 0, y = 0, orientation = 1;
    
    for( int i=0; i<sz; i++ ) {
        char cmd;
        int n;

        cmd = m[i].a;
        n = m[i].b;
        switch( cmd ) {
            case 'R':
                orientation = MOD(orientation + (n / 90), 4);
                break;
            case 'L':
                orientation = MOD(orientation - (n / 90), 4);
                break;
            case 'F':
                if( orientation == 0 )      y -= n;
                else if( orientation == 1 ) x += n;
                else if( orientation == 2 ) y += n;
                else if( orientation == 3 ) x -= n;
                break;
            case 'N': y -= n; break;
            case 'S': y += n; break;
            case 'E': x += n; break;
            case 'W': x -= n; break;
        }
    }
    return abs(x) + abs(y);
}

int part2(struct movement *m, int sz) {
    int x = 0, y = 0, orientation = 1, wx = 10, wy = -1;
    
    for( int i=0; i<sz; i++ ) {
        char cmd;
        int n;

        cmd = m[i].a;
        n = m[i].b;
        switch( cmd ) {
            case 'R':
                TODO
                break;
            case 'L':
                TODO
                break;
            case 'F':
                if( orientation == 0 )      y -= n * wy;
                else if( orientation == 1 ) x += n * wx;
                else if( orientation == 2 ) y += n * wy;
                else if( orientation == 3 ) x -= n * wx;
                break;
            case 'N': wy -= n; break;
            case 'S': wy += n; break;
            case 'E': wx += n; break;
            case 'W': wx -= n; break;
        }
    }
    return abs(x) + abs(y);
}
int main(int argc, char *argv[]) {
    struct movement *moves;
    int m_ptr = 0, i;
    char c;
    FILE *fd;

    moves = (struct movement *) malloc(sizeof(struct movement)*1000);

    if( !(fd = fopen("12-input.txt", "r")) )
        return puts("11-input: unable to open"), 1;

    for( m_ptr = 0; EOF != fscanf(fd, "%c%d\n", &c, &i); m_ptr++ ) {
        moves[m_ptr].a = c;
        moves[m_ptr].b = i;
    }
    printf("%d\n", part1(moves, m_ptr));
    printf("%d\n", part2(moves, m_ptr));
}

/*
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
*/

