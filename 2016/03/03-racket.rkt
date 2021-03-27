#lang racket
(define *triangles* (map (λ (x) (map string->number (string-split x))) (string-split (file->string "03-input.txt") "\n")))

(define (valid-triangle t)
  (let ([a (car t)] [b (cadr t)] [c (caddr t)])
    (and (> (+ a b) c) (> (+ a c) b) (> (+ b c) a))))
  
(define (process3 lst)
  (if (null? lst)
      '()
      (let ([xs (list (car lst) (cadr lst) (caddr lst))])
        (append (list (map car xs) (map cadr xs) (map caddr xs))
                (process3 (cdddr lst))))))

(println (length (filter valid-triangle *triangles*)))
(println (length (filter valid-triangle (process3 *triangles*))))
