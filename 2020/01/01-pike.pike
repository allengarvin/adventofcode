#!/usr/local/bin/pike

import Stdio;

int part1(array(int) n_arr) {
    for( int i; i<sizeof(n_arr); i++ )
        for( int j; j<sizeof(n_arr[1..]); j++ )
            if( n_arr[i] + n_arr[j] == 2020 )
                return n_arr[i] * n_arr[j];
}

int part2(array(int) n_arr) {
    for( int i; i<sizeof(n_arr); i++ )
        for( int j; j<sizeof(n_arr[1..]); j++ )
            for( int k; k<sizeof(n_arr[1..]); k++ )
                if( n_arr[i] + n_arr[j] + n_arr[k] == 2020 )
                    return n_arr[i] * n_arr[j] * n_arr[k];
}

int main() {
    object fd;
    array(int) numbers;

    fd = FILE();
    fd->open("01-input.txt", "r");
    numbers = map(fd->read() / "\n" - ({""}), lambda (string s) { return (int) s; });
    write("%d\n%d\n", part1(numbers), part2(numbers));
}
