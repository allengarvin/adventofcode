( configuration )
: srcfile       s" 02-input.txt" ;

80 Constant max-line
Create line-buffer max-line 2 + allot

0 Value fd-in

variable paper
variable boxtmp
variable ribbon

\ boxtmp 4 cells allot
create boxtmp 0 , 0 , 0 , 0 ,

\ via rosetta code:
defer less?   ' < is less?
 
: sort { array len -- }
  1 begin dup len u<= while 2* 1+ repeat { gap }
  begin gap 2 = if 1 else gap 5 11 */ then dup to gap while
    len gap do
      array i cells +
      dup @ swap         ( temp last )
      begin gap cells -
            array over u<=
      while 2dup @ less?
      while dup gap cells + over @ swap !
      repeat then
      gap cells + !
    loop
  repeat ;

: 3dup                          dup 2over rot ;
: 4rot                          swap 2swap ;
: box-init      (   --   )      1 boxtmp ! ;
: box-incr      (   --   )      boxtmp @ 1+ boxtmp ! ;
: box-push      ( n --   )      boxtmp dup @ cells + ! box-incr ;
: box-index     ( n -- n )      boxtmp swap cells + @ ;
: area          ( n n -- n )    * ;
: box-side      ( n n -- n n )  box-index swap box-index ;
: box-debug     (   --   )      1 box-index 2 box-index 3 box-index . . . cr ;
: box-paper     (   --   )      \ box-debug
                                1 2 box-side area 
                                1 3 box-side area 
                                2 3 box-side area 3dup min min 4rot + + 2 * + ;
: box-calc      ( n --   )      line-buffer swap evaluate box-push box-push box-push box-paper ;
: box-sort      ( addr -- )     -1 boxtmp ! boxtmp 4 sort ;
: box-2least    (   --   )      1 box-index 2 box-index + 2 * ;
: ribbon-calc   (   --   )      box-2least 1 box-index 2 box-index 3 box-index * * + ;
: ribbon-add    ( n --   )      ribbon @ + ribbon ! ;
: paper-add     ( n --   )      paper @ + paper ! ;
: isint         ( n -- n )      dup 48 >= swap 57 <= and ;

: init          (   --   )      0 paper ! 
                                0 ribbon ! ;
: open          (   --   )      srcfile r/o open-file throw to fd-in ;
: replace-x     ( n --   )      dup line-buffer swap + c@ 120 = if 32 swap line-buffer + c! else drop then ;
: process       dup 0 do i replace-x loop ;
: scan
        begin
            line-buffer max-line fd-in read-line throw
        while 
            box-init
            process
            box-calc
            paper-add
            box-sort
            ribbon-calc
            ribbon-add
        repeat ;

init open scan
cr ." Prob 1: " paper @ .
cr ." Prob 2: " ribbon @ . cr
bye
