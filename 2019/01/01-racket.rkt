#lang racket

(define *masses* (map string->number (string-split (file->string "01-input.txt") "\n")))

(define (sum list) (apply + list))
(define (fuel mass recurse?)
  (let ([f (- (quotient mass 3) 2)])
    (if (< f 0)
        0
        (if recurse?
            (+ f (fuel f #t))
            f))))

(println (sum (map (λ (m) (fuel m #f)) *masses*)))
(println (sum (map (λ (m) (fuel m #t)) *masses*)))
