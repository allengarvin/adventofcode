#lang racket

(define *answers* (string-split (file->string "06-input.txt") "\n\n"))

(define *answer-sets*
  (map (λ (x)
          (map string->list (string-split x "\n")))
       *answers*))

(define (sum lst) (apply + lst))

(define (solve func s-list) (sum (map (λ (lst) (length (apply func lst))) s-list)))

(println (solve set-union *answer-sets*))
(println (solve set-intersect *answer-sets*))
