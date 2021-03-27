#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fd;
    char c;
    int current_floor = 0, basement_point = 0, i=1;

    if( !(fd = fopen("01-input.txt", "r")) ) {
        printf("01-input: unable to open\n");
        return 1;
    }
    while( (c = fgetc(fd)) != '\n' ) {
        if( c == '(' )
            current_floor++;
        else if( c == ')' )
            current_floor--;
        if( !basement_point && current_floor == -1 )
            basement_point = i;
        i++;
    }
    printf("%d\n", current_floor);
    printf("%d\n", basement_point);
}
    
