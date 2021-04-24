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

(define *prog-weights* (make-hash))

(define (generate-weights root progs)
  (let* ([wt (car (hash-ref progs root))]
         [subwt (apply + (for/list ([i (second (hash-ref progs root))])
                                 (generate-weights i progs)))])
    (hash-set! *prog-weights* root (+ wt subwt))
    (+ wt subwt)))

(define root-weight (generate-weights *root* *prog-hash*)) ; don't need this for anything

(define (drill-down root wt)
  (let ([groups (group-by (λ (s) (hash-ref *prog-weights* s)) (last (hash-ref *prog-hash* root)))])
    (if (= 2 (length groups))
        (let ([diff (apply - (map (λ (g) (hash-ref *prog-weights* (car g))) (sort groups (λ (a b) (> (length a) (length b))))))])
          (drill-down (caar (filter (λ (g) (= 1 (length g))) groups)) diff))
        (+ (car (hash-ref *prog-hash* root)) wt))))

(displayln (drill-down *root* 0))


  