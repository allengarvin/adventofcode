#!/usr/local/bin/pike

import Stdio;

int main(int argc, string argv) {
    object fd;
    string s;
    int p1, p2;

    fd = FILE();
    fd.open(argc == 1 ? "01-input.txt" : argv[1], "r");
    s = fd->gets();

    for( int i=0; i<strlen(s); i++ ) {
        p1 += s[i] == s[(i+1) % strlen(s)] ? s[i] - 48: 0;
        p2 += s[i] == s[(i+strlen(s)/2) % strlen(s)] ? s[i] - 48: 0;
    }
    write("%d\n%d\n", p1, p2);
}
