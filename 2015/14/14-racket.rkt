#lang racket

(define (parse1 str)
  (let ([n (cdr (regexp-match #px"[A-Za-z]+ can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds." str))])
    (map string->number n)))

(define (parse-deer str)
  (let ([xs (parse1 str)])
    (vector-append (make-vector (cadr xs) (car xs)) (make-vector (caddr xs) 0))))

(define *input* (string-split (file->string "14-input.txt") "\n"))
(define *deer* (map parse-deer *input*))

(define (vsum vec) (apply + (vector->list vec)))
(define (distance vec turn)
  (+
     (* (quotient turn (vector-length vec)) (vsum vec))
     (vsum (vector-copy vec 0 (remainder turn (vector-length vec))))))

(println (apply max (map (λ (d) (distance d 2503)) *deer*)))

(define (max-by xs) (- (length xs) (length (member (apply max xs) xs))))
(define (winner sec) (max-by (map (λ (d) (distance d sec)) *deer*)))
(println (apply max (map length (group-by identity (map winner (range 1 2503))))))



