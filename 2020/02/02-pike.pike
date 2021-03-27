#!/usr/local/bin/pike
import Stdio;

int main(int argc, array argv) {
    object fd;
    int problem1, problem2;

    fd = File();
    fd->open(argc == 1 ? "02-input.txt" : argv[1], "r");
    foreach( fd.read() / "\n" - ({""}), string line ) {
        int low, high, cnt;
        string char, passwd;

        sscanf(line, "%d-%d %s: %s", low, high, char, passwd);
        cnt = sizeof(passwd / char) - 1;
        if ( cnt >= low && cnt <= high )
            problem1++;
        cnt = (passwd[low-1] == char[0]) + (passwd[high-1] == char[0]);
        if( cnt == 1 )
            problem2++;
    }
    write(problem1 + "\n" + problem2 + "\n");
}
