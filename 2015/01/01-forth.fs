#! /usr/bin/gforth

( configuration )
: input         s" 01-input.txt" ;

( input buffer )
variable 'src
variable #src

variable fh

\ The following from 'text processing in Forth' by Andreas Wagner CC AT SA
: open          input r/o open-file throw fh ! ;
: close         fh @ close-file throw ;
: read          begin here 4096 fh @ read-file throw dup allot 0= until ;
: gulp          open read close ;
: start         here 'src ! ;
: finish        here 'src @ - #src ! ;
: strip         -1 #src +! ;
: slurp         start gulp finish strip ;

( process input )
variable oset
variable p2solv?

: init          -1 p2solv? ! ;
: part1         ." Part 1: " . cr ;
: part2         p2solv? @ if ." Part 2: " 1 oset @ + . cr p2solv? 1+ then ;
: basement?     dup -1 = if part2 then ;
: dir           41 = if -1 else 1 then ;
: pparens       dir + basement? ;
: process       0 0 oset ! begin oset @ #src @ u< while
                'src @ oset @ + c@ pparens 1 oset +! repeat ;

( procedures )
init slurp process part1
bye
