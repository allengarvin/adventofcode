#lang racket

(define *place*
  (map string->number
       (cdr (regexp-match #px"To continue, please consult the code grid in the manual.  Enter the code at row (\\d+), column (\\d+)."
                          (string-trim (file->string "25-input.txt"))))))

(define (sum xs) (apply + xs))

(define (solve place)
  (let* ([start 20151125] [p1 252533] [mod-p 33554393]
                          [up-to (+ (second place) (quotient (* (- (sum place) 1) (- (sum place) 2)) 2) -1)])
    (for/list ([i (range up-to)])
      (set! start (modulo (* start p1) mod-p)))
    start))

(println (solve *place*))