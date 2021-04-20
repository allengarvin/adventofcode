#lang racket

(define (read-grid)
  (list->vector
   (map (λ (line) (list->vector (map (λ (char) (if (char=? char #\#) 1 0))
                                     (string->list line))))
        (string-split (file->string "18-input.txt") "\n"))))

  
(define list2 (λ x (list x)))
(define (neighbors y x)
  (append
   (if (> y 0)
       (let ([yp (sub1 y)])
         (append (list2 yp x)
                 (if (> x 0) (list2 yp (sub1 x)) null)
                 (if (< x 99) (list2 yp (add1 x)) null)))
       null)
   (if (< y 99)
       (let ([yp (add1 y)])
         (append (list2 yp x)
                 (if (> x 0) (list2 yp (sub1 x)) null)
                 (if (< x 99) (list2 yp (add1 x)) null)))
       null)
   (if (> x 0) (list2 y (sub1 x)) null)
   (if (< x 99) (list2 y (add1 x)) null)))

(define *grid* (read-grid))
(define (test-cell pair)
  (let ([y (car pair)] [x (cadr pair)])
    (vector-ref (vector-ref *grid* y) x)))

(define (sum xs) (apply + xs))
(define (count-lights grid)
  (sum (vector->list (vector-map (λ (vs) (sum (vector->list vs))) grid))))

(define (new-state y x)
  (let ([current-state (test-cell (list y x))]
        [n-states (apply + (map test-cell (neighbors y x)))])
    (if (zero? current-state)
        (if (= 3 n-states) 1 0)
        (if (or (= 2 n-states) (= 3 n-states)) 1 0))))

(define (corner? j i) (or (and (= j 0) (= i 0))
                          (and (= j 0) (= i 99))
                          (and (= j 99) (= i 0))
                          (and (= j 99) (= i 99))))
(define (new-grid part2?)
  (for/vector ([j (range 100)])
    (for/vector ([i (range 100)])
      (if (and part2? (corner? j i)) 1 (new-state j i)))))

(define (part1)
  (for ([i (range 100)])
    (set! *grid* (new-grid false)))
  (count-lights *grid*))
  
(define (part2)
  (for ([i (range 100)])
    (set! *grid* (new-grid true)))
      (count-lights *grid*))

(println (part1))
(set! *grid* (read-grid))
(println (part2))