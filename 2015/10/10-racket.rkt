#lang racket
; requires a lot of memory to run

; function I wrote for another problem
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

(define (look-say number-string)
  (apply string-append
         (let ([n (group-by-list (string->list number-string))])
           (map (λ (xs) (string-append (number->string (length xs)) (string (car xs)))) n))))

(define (look-say-sequence n start)
  (define (helper i acc)
    (begin
      (and (= i 40) (println (string-length acc)))
      (if (< i n)
          (helper (add1 i) (look-say acc))
          (println (string-length acc)))))
  (helper 1 (look-say start)))
          
          
(define *input* (string-trim (file->string "10-input.txt")))
(look-say-sequence 50 *input*)
