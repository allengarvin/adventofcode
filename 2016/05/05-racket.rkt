#lang racket

; Part 1 only--SO SLOW

(require file/md5)

(define (make-hash hash n) (bytes->string/utf-8 (md5 (string-append hash (number->string n)))))

(define *seed* (string-trim (file->string "05-input.txt")))

(define (part1 len)
  (define (helper start acc)
    (if (= len (string-length acc))
        acc
        (for/first ([i (in-naturals start)] #:when (string-prefix? (make-hash *seed* i) "00000"))
          (helper (add1 i) (string-append acc (string (string-ref (make-hash *seed* i) 5)))))))
  (helper 0 ""))

(println (part1 8))