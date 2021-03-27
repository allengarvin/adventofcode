empty

0 Value fd
80 Constant max-line
Create line-buffer max-line 2 + allot

variable numbers
numbers 200 cells allot
variable nindex
0 nindex !



: srcfile       s" 01-input.txt" ;


\ -------------------- number array -------------------------

: num           numbers swap cells + @ ;

\ -------------------- process file -------------------------
: ++            dup @ 1+ swap ! ;
: num-insert    numbers nindex @ cells + !
                nindex ++ ;
: read-int      line-buffer swap evaluate ;
: open          srcfile r/o open-file throw to fd drop ;
: read          
        begin
            line-buffer max-line fd read-line throw 
        while
            read-int
            num-insert
        repeat 
        drop ;
: close         fd close-file throw ;
: slurp         open read close ;


\ -------------------- combinations -------------------------

: test-comb1     
        num swap num 
        2dup + 2020 = if * -1 else 2drop 0 then ;

: 2-        2 - ;

: 3dup { a b c } a b c a b c ; 

: 3drop         drop 2drop ;

: test-comb2     
        num rot num rot num rot
        3dup + + 2020 = if * * -1 else 3drop 0 then ;

: loop1
        nindex @ 1- 0 do i
            nindex @ swap 1+ do i j
                test-comb1 if cr ." Problem 1: " . cr then
            loop
        loop ;


: loop2
        nindex @ 2- 0 do i
            nindex @ 1- swap 1+ do i j
                swap drop
                nindex @ swap 1+ do i j k
                    test-comb2 if ." Problem 2: " . cr unloop unloop unloop exit then
                loop
            loop
        loop ;

slurp loop1 loop2 bye




