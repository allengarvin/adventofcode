#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

#define FNAME argc == 1 ? "01-input.txt" : argv[1]
#define MOD(a, b) ((a % b) + b) % b

char *file_contents(int argc, char *argv[]) {
    FILE *fd;
    struct stat st;
    char *s;

    if( stat(FNAME, &st) == -1 || !(fd = fopen(FNAME, "r")) ) {
        fprintf(stderr, "%s: inaccessible\n", FNAME);
        exit(1);
    }
    s = (char *) malloc(1 + st.st_size * sizeof(char));
    fgets(s, st.st_size, fd);
    return s;
}

int main(int argc, char *argv[]) {
    char *mv, *file_con;
    int orientation = 0, num, x=0, y=0, i;
    int visited[100000][2], visit_ptr = 1, part2 = 0;

    file_con = file_contents(argc, argv);

    for( mv = strtok(file_con, ", "); mv != NULL; mv = strtok(NULL, ", ") ) {
        orientation = MOD((mv[0] == 'R' ? orientation + 1 : orientation - 1), 4) ;
        mv++;
        sscanf(mv, "%d", &num);
        for( i=0; i<num; i++ ) {
            switch( orientation ) {
                case 0: y--; break;
                case 1: x++; break;
                case 2: y++; break;
                case 3: x--; break;
            }
            if( !part2 ) {
                for( int j=0; j<visit_ptr; j++ )
                    if( visited[j][0] == x && visited[j][1] == y ) {
                        part2 = abs(x) + abs(y);
                        break;
                    }
            }
            visited[visit_ptr][0] = x;
            visited[visit_ptr][1] = y;
            visit_ptr++;
        }
    }
    printf("%d\n", abs(x) + abs(y));
    printf("%d\n", part2);
}
