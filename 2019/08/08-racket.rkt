#lang racket

(define *size* (list 25 6))
(define *layer-size* (* (car *size*) (cadr *size*)))
(define *image* (string-trim (file->string "08-input.txt")))
(define (line->ints line) (map (λ (c) (- (char->integer c) 48)) (string->list line)))
(define *layers*
  (map line->ints (map (λ (n) (substring *image* n (+ n *layer-size*))) (range 0 (string-length *image*) *layer-size*))))

(define (list-count xs n)
  (if (null? xs)
      0
      (+ (if (equal? (car xs) n) 1 0) (list-count (cdr xs) n))))

(println (let ([least (car (sort *layers* (λ (a b) (< (list-count a 0) (list-count b 0)))))])
           (* (list-count least 1) (list-count least 2))))

(define (make-pixel ndx)
  (for/first ([layer *layers*] #:when (not (= (list-ref layer ndx) 2)))
    (if (= 1 (list-ref layer ndx)) "#" " ")))
    
(define *final-img* (map make-pixel (range *layer-size*)))

(let ([y (cadr *size*)] [x (car *size*)])
  (for ([i (range y)])
    (println (apply string-append (take (list-tail *final-img* (* x i)) x)))))

            

