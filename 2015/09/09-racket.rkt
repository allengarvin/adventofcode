#lang racket

(define (explode-by-line x) (string-split x "\n"))
(define (parse-dist x y) (list (map string->symbol (string-split x " to ")) (string->number y)))
(define (parse-line ln) (apply parse-dist (string-split (string-trim ln) " = ")))
(define (1flat lst) (if (null? lst) '() (append (list (caar lst) (cadar lst)) (1flat (cdr lst)))))
(define (each-cons lst) (if (null? (cdr lst)) '[] (cons (list (car lst) (cadr lst)) (each-cons (cdr lst)))))
(define (sum lst) (apply + lst))
(define (complete-path plist) (sum (map (λ (x) (hash-ref *dhash* x)) plist)))

(define *dist1* (map parse-line (explode-by-line (file->string "09-input.txt"))))
(define *distances* (append *dist1* (map (λ (x) (cons (reverse (car x)) (cdr x))) *dist1*)))
(define *paths* (map each-cons (permutations (remove-duplicates (map caar *distances*)))))
(define *dhash* (apply hash (1flat *distances*)))
(define *all-distances* (sort (map complete-path *paths*) <))

(println (car *all-distances*))
(println (last *all-distances*))
