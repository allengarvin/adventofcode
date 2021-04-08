#lang racket

(define (parse-items str)
  (let ([t (string-split str ": ")])
    (cons (car t) (string->number (cadr t)))))

(define (parse-sue str)
  (let ([sue (cdr (regexp-match #px"Sue (\\d+): (.*)" str))])
    (list (string->number (car sue)) (map parse-items (string-split (cadr sue) ", ")))))

(define *sues* (map parse-sue (string-split (file->string "16-input.txt") "\n")))
(define *gift* (list (cons "children" 3) (cons "cats" 7) (cons "samoyeds" 2) (cons "pomeranians" 3)
                     (cons "akitas" 0) (cons "vizslas" 0) (cons "goldfish" 5) (cons "trees" 3)
                     (cons "cars" 2) (cons "perfumes" 1)))

(define (functional-and a b) (and a b))
(define (reduce f xs) (and (not (empty? xs)) (foldl f (first xs) (rest xs))))

(define (part1 sue)
  (reduce functional-and 
          (let ((remember-list (cadr sue)))
            (map (λ (pair)
                   (let ([k (car pair)] [v (cdr pair)])
                     (equal? (assoc k remember-list) (assoc k *gift*)))) remember-list))))

(define (part2 sue)
  (reduce functional-and 
          (let ((remember-list (cadr sue)))
            (map (λ (pair)
                   (let* ([k (car pair)] [v (cdr pair)])
                     (cond [(or (string=? k "cats") (string=? k "trees")) (> v (cdr (assoc k *gift*)))]
                           [(or (string=? k "pomeranians") (string=? k "goldfish")) (< v (cdr (assoc k *gift*)))]
                           [else (equal? (assoc k remember-list) (assoc k *gift*))]))) remember-list))))

(println (caar (filter part1 *sues*)))
(println (caar (filter part2 *sues*)))