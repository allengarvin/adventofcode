#!/usr/bin/tclsh

proc solution {list n} {
    set v [expr 2020 - $n]
    if { [lsearch $list $v] > -1 } {
        return $v
    }
    return 0
}

proc part1 {list} {
    foreach n $list {
        set v [solution $list $n]
        if { $v != 0 } {
            return $v
        }
    }
    return 0
}

set fd  [open "01-input.txt"]
set fc  [read $fd]
close   $fd

set numbers [split [string trim $fc] "\n"]

proc avg {numbers} {
   set sum 0
   foreach number $numbers {
      set sum  [expr $sum + $number]
   }
   return sum
}

set p1 [part1 $numbers]
puts [expr $p1 * (2020 - $p1)]

for {set i 0} {$i < [llength $numbers]} {incr i} {
    for {set j [expr $i + 1]} {$j < [llength $numbers]} {incr j} {
        set a [lindex $numbers $i]
        set b [lindex $numbers $j]
        set c [solution $numbers [expr $a + $b]]
        if { $c != 0 } {
            puts [expr $a * $b * $c]
            exit 0
        }
    }
}

