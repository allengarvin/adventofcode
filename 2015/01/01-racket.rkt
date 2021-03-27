#lang racket

(define (paren->int c) (if (char=? c #\() 1 -1))

(define *input*
  (map paren->int ((compose string->list string-trim file->string) "01-input.txt")))

(define (traverse lst pos)
  (if (null? lst)
      '()
      (let ([p (+ pos (car lst))])
        (cons p (traverse (cdr lst) p)))))

(define *floors* (traverse *input* 0))

(println (last *floors*))
(println (add1 (index-of *floors* -1)))
