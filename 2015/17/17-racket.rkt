#lang racket

(define *containers* (map string->number (string-split (file->string "17-input.txt") "\n")))

(define (powerset xs)
  (define (powerset-helper xs n)
    (if (zero? n)
        null ; we'd prefer to leave off the empty set here
        (append (combinations xs n) (powerset-helper xs (sub1 n)))))
  (powerset-helper xs (length xs)))

(define *fill-150* (filter (λ (xs) (= 150 (apply + xs))) (powerset *containers*)))

(println (length *fill-150*))
(println
  (let ([n (apply min (map (λ (xs) (length (car xs)))
                           (group-by length *fill-150*)))])
    (length (filter (λ (xs) (= n (length xs))) *fill-150*))))