#lang racket

(define *registers* (make-hash))

(define (add-register x)
  (if (hash-has-key? *registers* x)
      x
      (begin
        (hash-set! *registers* x 0)
        x)))

(define (check-register x)
  (hash-ref *registers* x))

(define (!= a b) (not (= a b)))

(define (dec r v)
  (let ([rv (check-register r)])
    (hash-set! *registers* r (- rv v))))

(define (inc r v)
  (let ([rv (check-register r)])
    (hash-set! *registers* r (+ rv v))))

(define (parse-operation op)
  (cond [(string=? op "==") my-==]
        [(string=? op ">=") my->=]
        [(string=? op "<=") my-<=]
        [(string=? op "!=") my-!=]
        [(string=? op "<")  my-< ]
        [(string=? op ">")  my-> ]
        [(string=? op "inc") inc]
        [(string=? op "dec") dec]
        [else (error op)]))
     
(define (my-== r v) (=  (check-register r) v))
(define (my->= r v) (>= (check-register r) v))
(define (my-<= r v) (<= (check-register r) v))
(define (my-!= r v) (not (= (check-register r) v)))
(define (my-< r v) (< (check-register r) v))
(define (my-> r v) (> (check-register r) v))

(define (parse-expression expr)
  (match-define (list register operation val) (string-split expr))
  (list operation (add-register register) (string->number val)))
    
(define *statements* (map (λ (s) (map parse-expression (string-split s " if "))) (file->lines "08-input.txt")))

(define (run-test)
  (let ([maximum -1])
    (for ([op   (map first *statements*)]
          [test (map last *statements*)])
      (and (apply (parse-operation (car test)) (cdr test))
           (apply (parse-operation (car op)) (cdr op)))
      (set! maximum (apply max (cons maximum (hash-values *registers*)))))
    (list (apply max (hash-values *registers*)) maximum)))

(apply printf "~a~n~a~n" (run-test))
      
  

 