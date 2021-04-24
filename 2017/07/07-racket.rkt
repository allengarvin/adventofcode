#lang racket

(define (parse line)
  (define (parse-three a b c)
    (list a (string->number b) (string-split c ", ")))
  (define (parse-two a b)
    (list a (string->number b) null))
  (if (string-contains? line "->")
      (apply parse-three (cdr (regexp-match #px"([a-z]+) \\((\\d+)\\) -> (.*)" line)))
      (apply parse-two   (cdr (regexp-match #px"([a-z]+) \\((\\d+)\\)" line)))))


(define *programs* (map parse (file->lines "07-input.txt")))
(define *prog-names* (map car *programs*))
(define *prog-hash* (make-hash *programs*))

(define *root*
  (car (filter (λ (i)
                 (null? (filter (λ (j) (member i (last (hash-ref *prog-hash* j)))) *prog-names*))) *prog-names*)))

(displayln *root*)
; part 1 finished
  