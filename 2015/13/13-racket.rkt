#lang racket

(define (parse-happy line)
  (match (cdr (regexp-match #px"([A-Za-z]+) would ([a-z]+) (\\d+) happiness units by sitting next to ([A-Z][a-z]+)." line))
    [(list who how n whom)
     (cons (list who whom)
          (* (if (string=? how "gain") 1 -1) (string->number n)))]))

(define (uniq xs)
  (define (f xs acc)
    (if (null? xs)
        (reverse acc)
        (let ([c (car xs)])
          (if (member c acc)
              (f (cdr xs) acc)
              (f (cdr xs) (cons c acc))))))
  (f xs null))

; (rotate-cons '(a b c d)) -> '((a b) (b c) (c d) (d a))
(define (rotate-cons lst)
  (let ([first-save (first lst)])
    (define (f-helper xs 1st)
      (if (null? (cdr xs))
          (list (cons (car xs) (list first-save)))
          (cons (list (car xs) (cadr xs)) (f-helper (cdr xs) first-save))))
    (f-helper lst first-save)))

(define (assoc-value n xs)
  (let ([a (assoc n xs)])
    (if (false? a)
        0
        (cdr a))))

(define (sum xs) (apply + xs))
(define (nil-zero n) (if (false? n) 0 n))

(define *relations* (map parse-happy (string-split (file->string "13-input.txt") "\n")))
(define *people* (uniq (map caar *relations*)))

(define a (car (permutations *people*)))

(define (happiness xs)
  (sum (map (λ (pair) (+ (nil-zero (assoc-value pair *relations*)) (nil-zero (assoc-value (reverse pair) *relations*)))) (rotate-cons xs))))

(displayln (apply max (map happiness (permutations *people*))))
(displayln (apply max (map happiness (permutations (cons "You" *people*)))))


