#lang racket

(define (movement x)
  (cond
    [(char=? x #\^) 0-1i]
    [(char=? x #\v) 0+1i]
    [(char=? x #\<) -1+0i]
    [(char=? x #\>) 1+0i]))
  
(define *input*
  (map movement ((compose string->list string-trim file->string) "03-input.txt")))

(define (traverse lst pos)
  (if (null? lst)
      '[0]
      (let ([p (+ pos (car lst))])
        (cons p (traverse (cdr lst) p)))))

(define (traverse2 lst santa-pos robot-pos cnt)
  (if (null? lst)
      '[0]
      (let ([p (+ (if (even? cnt) santa-pos robot-pos) (car lst))])
        (cons p (traverse2 (cdr lst)
                           (if (even? cnt) p santa-pos)
                           (if (odd? cnt) p robot-pos)
                           (add1 cnt) )))))

(println (length (remove-duplicates (traverse *input* 0))))
(println (length (remove-duplicates (traverse2 *input* 0 0 0))))