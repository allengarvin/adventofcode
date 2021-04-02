#!/usr/local/bin/pike

import Stdio;

int main(int argc, array(string) argv) {
    array(int) floors;
    object fd;
    int fl;

    fd = FILE();
    fd->open(argc == 1 ? "01-input.txt" : argv[1], "r");
    floors = map(fd->read()[0..<1] / "", lambda (string c ) { return fl += c == ")" ? -1 : 1; });
    write("%d\n%d\n", floors[-1], search(floors, -1));
}
