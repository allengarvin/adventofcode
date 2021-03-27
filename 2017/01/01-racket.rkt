#lang racket

(define *digits* (string->list (string-trim (file->string "01-input.txt"))))
(define (sum lst) (apply + lst))
(define (captcha lst steps)
  (for/sum ([i (range (length lst))])
            (let ([a (list-ref lst i)]
                 [b (list-ref lst (modulo (+ i steps) (length lst)))])
              (if (char=? a b) (- (char->integer a) 48) 0))))
                  
(println (captcha *digits* 1))
(println (captcha *digits* (/ (length *digits*) 2)))