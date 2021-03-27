#lang racket

(define *messages* (string-split (file->string "06-input.txt") "\n"))

(define (zip l1 l2) (map cons l1 l2))
(define (msg-sets lst acc)
  (if (null? lst)
      (map (λ (x) (group-by identity x)) (map flatten acc))
      (msg-sets (cdr lst) (zip (map list (string->list (car lst))) acc))))

(define *decoded*
  (map (λ (x) (sort x (λ (a b) (> (length a) (length b)))))
       (msg-sets *messages* (build-list (string-length (car *messages*)) (λ (x) (list))))))

(displayln (list->string (flatten (map caar *decoded*))))
(displayln (list->string (flatten (map (compose car last) *decoded*))))
    
    