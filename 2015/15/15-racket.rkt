#lang racket


(define *ingredients* (map (λ (line)
                             (map (λ (part) (string->number (last (string-split part " "))))
                                  (string-split line ", ")))
                           (string-split (file->string "15-input.txt") "\n")))

; all the ways to add four positive integers to sum to 100
(define (partition max-n elements)
  (define (helper m e prefix)
    (if (= e 2)
        (for/list ([i (range 1 m)]) (append prefix (list i (- m i))))
        (apply append (for/list ([i (range 1 m)])
                        (helper (- m i) (sub1 e) (cons i prefix))))))
  (helper max-n elements null))

(define (mul xs) (apply * xs))
(define (sum xs) (apply + xs))
(define (all-but-last xs) (take xs (sub1 (length xs))))
(define zip (λ xs (apply map list xs)))

; add any number of lists that are all the same length. (add-lists '(1 2) '(3 4)) => (3 6)
(define add-lists (λ xs (map sum (apply zip xs))))
(define (make-positive xs) (map (λ (n) (if (negative? n) 0 n)) xs))
(define (multiply-by-scaler xs n) (map (λ (x) (* x n)) xs))
(define (multiply-matrix matrix array) (map (λ (xs n) (multiply-by-scaler xs n)) matrix array))

(define *100-partitioned* (partition 100 4))
; > (multiply-matrix *ingredients* (car *100-partitioned*))
; '((5 -1 0 0 5) (-1 3 0 0 1) (0 -1 4 0 6) (-97 0 0 194 776))
;> (multiply-matrix (map all-but-last *ingredients*) (car *100-partitioned*))
;'((5 -1 0 0) (-1 3 0 0) (0 -1 4 0) (-97 0 0 194))

(define a (car *100-partitioned*))

(define (cookie part ingredients)
  (let ([score (mul (make-positive (apply add-lists (multiply-matrix (map all-but-last ingredients) part))))]
        [calories (sum (map last (multiply-matrix ingredients part)))])
    (list score calories part)))

(define *cookies* (map (λ (p) (cookie p *ingredients*)) *100-partitioned*))
    
(println (apply max (map car *cookies*)))
(println (apply max (map car (filter (λ (xs) (= (second xs) 500)) *cookies*))))

  ;(make-positive (sum (apply add-lists (multiply-matrix part (all-but-last xs))))))