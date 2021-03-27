<?php
    $lines = array_map("intval", explode("\n", trim(file_get_contents("01-input.txt"))));
    foreach( $lines as $num ) {
        $val = 2020 - $num;
        if( in_array($val, $lines) ) {
            print_r( ($val * $num) . "\n");
            break;
        }
    }
    for( $i = 0; $i < sizeof($lines); $i++ ) {
        for( $j = $i+1; $j < sizeof($lines); $j++ ) {
            $a = $lines[$i];
            $b = $lines[$j];
            $val = 2020 - $a - $b;
            if( in_array($val, $lines) ) {
                print_r( ($val * $a * $b) . "\n");
                exit(0);
            }
        }
    }
?>
