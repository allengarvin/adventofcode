#lang racket

; from https://exercism.io/tracks/racket/exercises/all-your-base/solutions/dd263d29a1544b579ba6457e238ac146
(define (rebase list-digits in-base out-base)
  (if (or (< in-base 2) (< out-base 2)
          (ormap negative? list-digits)
          (ormap (curry <= in-base) list-digits))
      #f
      (to (from list-digits in-base) out-base)))

(define (zip l1 l2) (map list l1 l2))
(define (powers len) (reverse (range len)))
(define (_from in-base item)
  (* (first item) (expt in-base (second item))))

(define (from list-digits in-base)
  (let ([len (length list-digits)]
        [from-in-base ((curry _from) in-base)])
    (apply +
           (map from-in-base
                (zip list-digits (powers len))))))

(define (_to num out-base)
  (if (< num out-base) num
      (list (to (quotient num out-base) out-base)
            (remainder num out-base))))

(define (to num out-base)
  (flatten (_to num out-base)))
;------
(define *old-pass* (string-trim (file->string "11-input.txt")))
(define (password->base26 p)
  (map (λ (c) (- (char->integer c) 97)) (string->list p)))
(define (base26->int n)
  (string->number (apply string-append
                         (map number->string
                              (rebase n 26 10)))))
(define (int->base26 n)
  (rebase (map (λ (c) (- (char->integer c) 48))
                                         (string->list (number->string n))) 10 26))
  
 
(define (password->integer p) (base26->int (password->base26 p)))
  
(define (integer->password i)
  (apply string-append (map (λ (n) (string (integer->char (+ n 97))))
                            (int->base26 i))))

(define (test1 xs)
  (define (helper ys p1 p2)
    (cond [(null? ys) #f]
          [(= (car ys) (add1 p2) (add1 (add1 p1))) #t]
          [else (helper (cdr ys) p2 (car ys))]))
  (helper (cddr xs) (car xs) (cadr xs)))

(define (test2 xs) (not (or
                    (member 8 xs) ; i
                    (member 11 xs); l
                    (member 14 xs); o
                    )))
(define (test3 xs)
  (define (helper xs acc)
    (cond [(null? xs) acc]
          [(null? (cdr xs)) acc]
          [(= (car xs) (cadr xs)) (helper (cddr xs) (add1 acc))]
          [else (helper (cdr xs) acc)]))
  (> (helper xs 0) 1))

(define (valid-pass xs) (and (test1 xs) (test2 xs) (test3 xs)))

(define (next-password p)
  (let ([n (add1 (password->integer p))])
    (for/first ([i (range n (+ n 10000000))]
                #:when (valid-pass (int->base26 i)))
      (integer->password i))))

(define *part1* (next-password *old-pass*))
(displayln *part1*)
(displayln (next-password *part1*))
    