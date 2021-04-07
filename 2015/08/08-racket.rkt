#lang racket
(current-namespace (make-base-namespace))

(define *strings* (string-split (file->string "08-input.txt") "\n"))
(define *compact* (map (λ (s) (eval (call-with-input-string s read))) *strings*))
(define *expand* (map (λ (s) (string-append "\"" (string-replace (string-replace s "\\" "\\\\") "\"" "\\\"") "\"")) *strings*))

(define (sum xs) (apply + xs))
(define (string-length-diff xs ys) (sum (map (λ (s1 s2) (- (string-length s1) (string-length s2))) xs ys)))

(println (string-length-diff *strings* *compact*))
(println (string-length-diff *expand* *strings*))