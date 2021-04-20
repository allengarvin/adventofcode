#lang racket

(define *nums* (map string->number (string-split (file->string "24-input.txt") "\n")))

(define (sum xs) (apply + xs))
(define (mul xs) (apply * xs))

(define (find-min numbers num-partitions)
  (let ([r-nums (reverse numbers)]
        [target (quotient (sum numbers) num-partitions)])
    (for/first ([i (range 0 (length numbers))] #:when (>= (sum (take r-nums i)) target))
      i)))

(define (test-combinations numbers n target)
  (filter (λ (xs) (= (sum xs) target)) (combinations numbers n)))

(define (least numbers num-partitions)
  (let ([target (quotient (sum numbers) num-partitions)]
        [min-size (find-min numbers num-partitions)])
    (for*/first ([i (range min-size (- (length numbers) min-size))]
                 [xs (list (test-combinations numbers i target))]
                #:when (not (null? xs)))
      xs)))

(println (apply min (map mul (least *nums* 3))))
(println (apply min (map mul (least *nums* 4))))
