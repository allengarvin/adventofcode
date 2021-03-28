#lang racket

(define x (map string->number (string-split (string-trim (file->string "04-input.txt")) "-")))
(define *lo* (car x))
(define *hi* (cadr x))

(define (group-by-list gr)
    (define (group-help ys ps)
      (cond [(and (null? ys) (null? ps)) null]
            [(null? ys) (list ps)]
            [(null? ps) (group-help (cdr ys) (list (car ys)))]
            [#t (let ([prev (car ps)])
                  (if (equal? (car ys) prev)
                      (group-help (cdr ys) (cons prev ps))
                      (cons ps (group-help (cdr ys) (list (car ys))))))]))
    (group-help gr null))

(define (sort-string str) (list->string (sort (string->list str) char<?)))
(define (ascending? n) (let ([ns (number->string n)]) (string=? ns (sort-string ns))))
(define (part1 n) (>= (apply max (map length n)) 2))
(define (part2 n) (member 2 (map length n)))
(define *asc* (map (compose group-by-list string->list number->string) (filter ascending? (range *lo* *hi*))))

(println (length (filter part1 *asc*)))
(println (length (filter part2 *asc*)))






