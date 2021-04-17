#lang racket

(define (parse-string string)
  (map string->number (cdr (regexp-match #px"^#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)" string))))

(define *claims* (map parse-string (string-split (file->string "03-input.txt") "\n")))

(define *cloth* (vector-map (λ (v) (make-vector 1000 null)) (make-vector 1000)))

(define (functional-and a b) (and a b))
(define (reduce f xs) (and (not (empty? xs)) (foldl f (first xs) (rest xs))))

(define (make-claim xs)
  (match xs [(list claim-no x y width length)
             (for* ([i (range x (+ x width))]
                    [j (range y (+ y length))])
               (vector-set! (vector-ref *cloth* j) i (cons claim-no (vector-ref (vector-ref *cloth* j) i))))]))

(define (test-claim xs)
  (reduce functional-and
          (match xs [(list claim-no x y width length)
                     (for*/list ([i (range x (+ x width))]
                                 [j (range y (+ y length))])
                       (equal? (list claim-no) (vector-ref (vector-ref *cloth* j) i)))])))

(define foo (map make-claim *claims*))
(println (apply + (vector->list (vector-map (λ (vs) (vector-length (vector-filter (λ (v) (< 1 (length v))) vs))) *cloth*))))
(println (caar (filter test-claim *claims*)))



    
  

