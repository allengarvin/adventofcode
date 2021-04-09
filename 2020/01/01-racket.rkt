#lang racket
(define *numbers* (map string->number (file->lines "01-input.txt")))

(define sum (λ (lst) (apply + lst)))
(define mul (λ (lst) (apply * lst)))

(println (mul (filter (λ (x) (member (- 2020 x) *numbers*)) *numbers*)))
(println (sqrt (mul (map mul (filter (λ (pair) (member (- 2020 (sum pair)) *numbers*)) (combinations *numbers* 2))))))
