#lang racket

; TODO: refactor. Very slow because of inefficient list referencing (lazy--need to add vector funcs for list funcs)

(define *numbers* (list->vector (map string->number (string-split (file->string "09-input.txt") "\n"))))

(define (sum xs) (apply + xs))
(define (vector-sum vs) (sum (vector->list vs)))

(define (test-no-sum n vs)
  (null? (filter (λ (x) (= x n)) (map sum (combinations (vector->list vs) 2)))))

(define (bad-index xs)
   (for/first ([i (range 25 (vector-length xs))]
               #:when (test-no-sum (vector-ref xs i) (vector-copy xs (- i 25) i)))
     i))

(define *ndx* (bad-index *numbers*))
(println (vector-ref *numbers* *ndx*))

(define (part2 xs ndx)
  (let* ([n (vector-ref xs ndx)]
         [rng (filter (λ (zs) (= n (vector-sum (vector-copy xs (car zs) (add1 (cadr zs)))))) (combinations (range 0 (vector-length xs)) 2))]
         [ys (vector->list (vector-copy xs (caar rng) (add1 (cadar rng))))])
    (+ (apply min ys) (apply max ys))))

(println (part2 *numbers* *ndx*))