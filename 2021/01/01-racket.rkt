#lang racket
(require srfi/1)
(define *numbers* (map string->number (file->lines "01-input.txt")))
(define (count-ascending lst)
    (length (filter (lambda (x) (apply < x)) (map list (drop-right lst 1) (cdr lst)))))
(define (window3 lst)
  (if (empty? (cddr lst))
      '()
      (cons (+ (car lst) (cadr lst) (caddr lst)) (window3 (cdr lst)))))
     
(println (count-ascending *numbers*))
(println (count-ascending (window3 *numbers*)))