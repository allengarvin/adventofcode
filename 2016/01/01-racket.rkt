#lang racket
(require data/monad data/applicative)
(require megaparsack megaparsack/text)

(define *dirs* '(0-i 1 0+i -1))
(define move/p
  (do [x <- letter/p]
      [n <- integer/p]
    (pure (list x n))))
(define (traverse mv-list dir pos)
  (if (null? mv-list)
      '[]
      (let* ([p (parse-result! (parse-string move/p (car mv-list)))]
             [d (modulo (if (char=? (car p) #\R ) (add1 dir) (sub1 dir)) 4) ]
             [n (cadr p)])
        (append (map (λ (i) (+ pos (* i (list-ref *dirs* d)))) (range 1 (add1 n)))
                (traverse (cdr mv-list) d (+ pos (* n (list-ref *dirs* d))))))))
(define (first-duplicate lst acc)
  (let ([c (car lst)])
    (if (member c acc)
        c
        (first-duplicate (cdr lst) (cons c acc)))))
(define (taxi-dist pos) (+ (abs (real-part pos)) (abs (imag-part pos))))

(define *moves* (string-split (string-trim (file->string "01-input.txt")) ", "))
(define *visited* (traverse *moves* 0 0))

(println (taxi-dist (last *visited*)))
(println (taxi-dist (first-duplicate *visited* '[])))