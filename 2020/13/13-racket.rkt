#lang racket

(require (only-in math/number-theory solve-chinese))

(define (file-lines filename) (string-split (file->string filename) "\n"))
(define *departure* (string->number (car (file-lines "13-input.txt"))))
(define *buses* (map string->number (string-split (cadr (file-lines "13-input.txt")) ",")))

(define (solve1 start-time buses)
  (let ([answer #f])
    (for/first ([i (range start-time (* start-time 1000))]
                #:when (for/first ([b buses] #:when (and (number? b) (zero? (remainder i b))))
                         (set! answer (* b (- i start-time)))
                         answer))
      answer)))
                       
(define *congruences*
  (filter identity
          (for/list ([n (range (length *buses*))]
                      [p *buses*]) (if (number? p) (modulo (- p n) p) #f))))
(define *primes* (filter identity *buses*))

(println (solve1 *departure* *buses*))                                          
(println (solve-chinese *congruences* *primes*))


