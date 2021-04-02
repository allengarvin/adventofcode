#!/usr/local/bin/pike

import Stdio;
import Array;

int atoi(string s) { return (int) s; }

int paper(array(int) d) { return 2*(d[0]*d[1] + d[1]*d[2] + d[0]*d[2]) + d[0]*d[1]; }
int ribbon(array(int) d) { return 2*(d[0] + d[1]) + d[0]*d[1]*d[2]; }

int main(int argc, array(string) argv) {
    Stdio.File fd = Stdio.File();
    array(array(int)) presents;

    fd->open("02-input.txt", "r");
    presents = map(fd->read() / "\n" - ({""}), lambda (string p) { return sort(map(p / "x", atoi)); });
    
    write("%d\n%d\n", Array.sum(map(presents, paper)), Array.sum(map(presents, ribbon)));
}

