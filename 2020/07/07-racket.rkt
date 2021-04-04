#lang racket

(define (parse-line s)
  (let* ([e (cdr (regexp-match #px"^(\\w+ \\w+) bags contain (.*)\\.$" s))]
         [a (car e)]
         [b (cadr e)])
    (list a
          (if (string-contains? b "no other")
              null
              (map (λ (c)
                     (let ([l (cdr (regexp-match #px"(\\d+) (\\w+ \\w+) bags?" c))])
                       (cons (cadr l) (string->number (car l)))))
                   (string-split b ", "))))))

(define *lines* (string-split (file->string "07-input.txt") "\n"))
(define *bag-tree* (map parse-line *lines*))


(define (functional-or a b) (or a b))
(define (reduce f xs)
  (and (not (empty? xs)) (foldl f (first xs) (rest xs))))
(define (sum xs) (apply + xs))

; TODO: memo-ize contains to prevent re-execution
(define (contains? top-bag bag)
  (let ([contents (cadr (assoc top-bag *bag-tree*))])
    (cond [(null? contents) #f]
          [(assoc bag contents) #t]
          [else (reduce functional-or (map (λ (x) (contains? (car x) bag)) contents))])))

(define (total-bags top-bag)
  (let ([contents (assoc top-bag *bag-tree*)])
    (cond [(null? contents) 1]
          [else (add1 (sum (map (λ (c) (* (cdr c) (total-bags (car c)))) (cadr contents))))])))

(println (length (filter (λ (b) (contains? (car b) "shiny gold")) *bag-tree*)))
(println (sub1 (total-bags "shiny gold")))
        
    

