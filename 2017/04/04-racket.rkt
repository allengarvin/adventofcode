#lang racket
(define (valid lst func) (filter (λ (x) (not (check-duplicates (map func x)))) lst))
(define (anagramer x) (sort (map char->integer (string->list x)) <))

(define *passphrases* (map string-split (string-split (file->string "04-input.txt") "\n")))
(define *part1* (valid *passphrases* identity))

(println (length *part1*))
(println (length (valid *part1* anagramer)))
