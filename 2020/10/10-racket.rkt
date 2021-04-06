#lang racket

(define *jolts*
  (let ([j (sort (map string->number (string-split (file->string "10-input.txt") "\n")) <)])
    (append (cons 0 j) (list (+ (last j) 3)))))

(define *diffs* (group-by identity (map (λ (a b) (abs (- a b)))
                               (take *jolts* (sub1 (length *jolts*)))
                               (cdr *jolts*))))
(define *groups*
  (map (λ (xs) (cons (car xs) (length (cdr xs)))) *diffs*))

(println (* (cdr (assoc 1 *groups*)) (cdr (assoc 3 *groups*))))

; assumes sorted
(define (contiguous xs)
  (define (contig-helper xs acc)
    (if (null? xs)
        (map reverse (reverse acc))
        (let ([i (car xs)])
          (if (null? acc)
              (contig-helper (cdr xs) (list (list i)))
              (let ([j (caar acc)])
                (if (= (sub1 i) j)
                    (contig-helper (cdr xs) (cons (cons i (car acc)) (cdr acc)))
                    (contig-helper (cdr xs) (cons (list i) acc))))))))
  (contig-helper xs null))

; differences aren't large, otherwise I'd make a tail-recursive or memo-ized version
 (define (tribonacci n)
   (cond [(= n 0) 0]
         [(= n 1) 0]
         [(= n 2) 1]
         [else (+ (tribonacci (- n 1))
                  (tribonacci (- n 2))
                  (tribonacci (- n 3)))]))

(println (apply * (map (λ (xs) (tribonacci (add1 (length xs)))) (contiguous *jolts*))))
