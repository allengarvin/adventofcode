#lang racket
(define (to-binary str)
  (string->number 
    (string-replace
     (string-replace
      (string-replace 
        (string-replace str "B" "1") "R" "1") "L" "0") "F" "0") 2))

(define *seats* (sort (map to-binary (file->lines "05-input.txt")) <))

(println (last *seats*))

(println (for/first ([x (in-range (first *seats*) (last *seats*))] #:when (not (member x *seats*))) x))
