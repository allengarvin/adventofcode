#lang racket

(require racket/stream)

(define *forest*
  (list->vector (map (lambda (ln) (list->vector (string->list ln)))
                                  (string-split (file->string "03-input.txt") "\n"))))

(define (sum xs) (apply + xs))
(define (mul xs) (apply * xs))

(define (traverse forest x-step y-step)
  (for/list ([x (in-naturals)]
             [y (in-range 0 (vector-length forest) y-step)])
    (let ([i (* x x-step)]
          [row (vector-ref forest y)])
      (if (char=? #\# (vector-ref row (modulo i (vector-length row))))
          1
          0))))
    
(println (sum (traverse *forest* 3 1)))
  
(define *part2-steps* '((1 1) (3 1) (5 1) (7 1) (1 2)))

(println (mul (map (λ (xs) (sum (traverse *forest* (car xs) (cadr xs)))) *part2-steps*)))


