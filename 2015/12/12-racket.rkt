#lang racket

(require json)
(define *json* (string->jsexpr (file->string "12-input.txt")))

(define (sum xs) (apply + xs))

(define (test-exclude js exclude)
  (for/first (((key val) (in-hash js)) #:when (and (string? val) (string=? val exclude))) val))
    

(define (traverse j exclude)
  (cond [(hash? j) (if (test-exclude j exclude)
                       0
                       (sum (for/list (((key val) (in-hash j)))
                            (traverse val exclude))))]
        [(string? j) 0]
        [(integer? j) j]
        [(list? j) (sum (map (λ (x) (traverse x exclude)) j))]
        [else (println j)]))
  
(println (traverse *json* "NONSENSE-STRING"))
(println (traverse *json* "red"))