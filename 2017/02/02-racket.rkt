#lang racket
(define *grid* (map (λ (x) (sort (map string->number (string-split x)) <)) (string-split (file->string "02-input.txt") "\n")))

(define (sum list) (apply + list))
(define (part2-filter lst)
  (car (filter number?
          (map (λ (x) (let ([a (cadr x)] [b (car x)])
                      (if (zero? (modulo a b))
                       (/ a b)
                       #f)))
          (combinations lst 2)))))

(println (sum (map (λ (x) (- (last x) (car x))) *grid*)))
(println (sum (map part2-filter *grid*)))

