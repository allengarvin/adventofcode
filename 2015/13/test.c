#include <stdio.h>

#define MOD(A, B) (A % B < 0) ? B + (A % B) : (A % B)

int main() {
    printf("%d\n", MOD(-1, 8));
    printf("%d\n", MOD(8, 8));
    printf("%d\n", MOD(9, 8));
}
