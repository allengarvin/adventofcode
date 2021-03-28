#lang racket

(define rooms (string-split (file->string "04-input.txt") "\n"))

(define (sector-id str)
  (string->number (car (string-split (last (string-split str "-")) "["))))

(define (prefix rm)
  (string-join ((compose reverse cdr reverse) (string-split rm "-")) "-"))

(define (cksum str)
  (string-replace (cadr (string-split (car (reverse (string-split str "-"))) "[")) "]" ""))

(define (letters str)
  (group-by identity (string->list (string-join (cdr (reverse (string-split str "-"))) ""))))

(define (group-string str)
  (group-by identity (string->list (string-join (string-split str "-") ""))))

(define (sort-helper as bs)
  (if (= (length as) (length bs))
      (< (char->integer (car as)) (char->integer (car bs)))
      (> (length as) (length bs))))

(define (first-n lst n)
  (if (zero? n) null (cons (car lst) (first-n (cdr lst) (sub1 n)))))

(define a (cksum (car rooms)))
(define b (list->string (map car (sort (letters (car rooms)) sort-helper))))

(define (valid rm)
  (let ([ck (cksum rm)]
        [lt (list->string (first-n (map car (sort (letters rm) sort-helper)) 5))])
    (string=? ck lt)))

(define (sum lst) (apply + lst))
(define (zip xs ys) (map list xs ys))

(define *valid-rooms*
  (let ([rms (filter valid rooms)])
    (zip (map sector-id rms) (map prefix rms))))

(define (cipher n str)
  (let ([xs (string->list str)])
    (define (cipher-list xs)
      (cond [(null? xs) null]
            [(char=? #\- (car xs)) (cons #\space (cipher-list (cdr xs)))]
            [#t (cons (integer->char (+ (modulo (+ (- (char->integer (car xs)) 97) n) 26) 97)) (cipher-list (cdr xs)))]))
    (list n (list->string (cipher-list xs)))))

(println (sum (map car *valid-rooms*)))
(println (caar
          (filter (λ (p) (if (string-contains? (cadr p) "northpole") (car p) #f))
                  (map (λ (p) (apply cipher p)) *valid-rooms*))))
