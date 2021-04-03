#lang racket


(define *grid* (vector-map (lambda (x) (make-vector 1000)) (make-vector 1000)))

(define (sum xs) (apply + xs))

(define (grid-query v x y) (vector-ref (vector-ref v y) x))
(define (grid-count v)
  (sum (for*/list ([y (range 0 1000)]) (sum (vector->list (vector-ref v y))))))
           

(define (modify v func x1 y1 x2 y2)
  (for* ([y (range y1 (add1 y2))]
         [x (range x1 (add1 x2))])
         (let* ([row (vector-ref v y)]
                [val (vector-ref row x)])
           (vector-set! row x (func val)))))

(define (turn-on  x) 1)
(define (turn-off x) 0)
(define (toggle   x) (if (zero? x) 1 0))

(define (turn-on-2  x) (add1 x))
(define (turn-off-2 x) (if (zero? x) 0 (sub1 x)))
(define (toggle-2   x) (+ x 2))

(define (parse-line s)
  (let ([xs (cdr (regexp-match #px"^(.*?) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$" s))])
    (cons (car xs) (map string->number (cdr xs)))))

(define *commands* (map parse-line (string-split (file->string "06-input.txt") "\n")))
(define a (car *commands*))

(define (part1-func xs)
  (let ([cmd (car xs)])
        (cond [(string=? "turn on" cmd) turn-on]
              [(string=? "turn off" cmd) turn-off]
              [(string=? "toggle" cmd) toggle]
              [else (error cmd)])))

(define (part1-map xs)
  (apply modify (cons *grid* (cons (part1-func xs) (cdr xs)))))

(define (part2-func xs)
  (let ([cmd (car xs)])
        (cond [(string=? "turn on" cmd) turn-on-2]
              [(string=? "turn off" cmd) turn-off-2]
              [(string=? "toggle" cmd) toggle-2]
              [else (error cmd)])))

(define (part2-map xs)
  (apply modify (cons *grid* (cons (part2-func xs) (cdr xs)))))

(for-each part1-map *commands*)
(println (grid-count *grid*))
(part1-map (list "turn off" 0 0 999 999))
(for-each part2-map *commands*)
(println (grid-count *grid*))


