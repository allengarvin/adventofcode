#lang racket

(define *presents*
  (map (lambda (x) (sort (map string->number (string-split x "x")) <))
       (string-split (file->string "02-input.txt"))))

(define (sum xs) (apply + xs))

(define (paper xs)
  (let ([a (car xs)] [b (cadr xs)] [c (caddr xs)])
    (+ (* a b) (* 2 (+ (* a b) (* a c) (* b c))))))

(define (ribbon xs)
  (let ([a (car xs)] [b (cadr xs)] [c (caddr xs)])
    (+ (* 2 (+ a b)) (* a b c))))

(println (sum (map paper *presents*)))
(println (sum (map ribbon *presents*)))
