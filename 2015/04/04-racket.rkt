#lang racket

(require file/md5)
(define *initial-hash* (string-trim (file->string "04-input.txt")))

(define (make-hash hash n) (bytes->string/utf-8 (md5 (string-append hash (number->string n)))))
  
(define (solve hash prefix n)
  (for/first ([i (in-naturals n)] #:when (string-prefix? (make-hash hash i) prefix)) i))

(define *part1* (solve *initial-hash* (make-string 5 #\0) 1))
(define *part2* (solve *initial-hash* (make-string 6 #\0) *part1*))

(println *part1*)
(println *part2*)
            