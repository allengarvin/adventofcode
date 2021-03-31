#lang racket

(define *str* (string-split (file->string "02-input.txt") "\n"))
(define *len* (string-length (car *str*)))

(define (common a b)
  (cond [(= (string-length a) 0) null]
        [(char=? (string-ref a 0) (string-ref b 0)) (cons (string-ref a 0) (common (substring a 1) (substring b 1)))]
        [else (common (substring a 1) (substring b 1))]))

(define (repeat-n n) (λ (lst) (member n lst)))
(define *freqs* (map (λ (s) (map length (group-by identity (string->list s)))) *str*))

(println (* (length (filter (repeat-n 2) *freqs*)) (length (filter (repeat-n 3) *freqs*))))

(define (part2-test xs)
  (let ([n (common (car xs) (cadr xs))])
    (if (= (length n) (sub1 *len*))
        (list->string n)
        #f)))

(display (list->string (apply common (car (filter part2-test (combinations *str* 2))))))
        