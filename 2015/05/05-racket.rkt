#lang racket

(define *strings* (string-split (file->string "05-input.txt") "\n"))
(define *doubles*
  (map (lambda (c)
         (let ([l (string (integer->char c))])
           (string-append l l))) (range 97 123)))

(define (vowel? c) (not (null? (filter (lambda (v) (char=? c v)) (list #\a #\e #\i #\o #\u)))))
  
(define (count-vowels s)
  (if (zero? (string-length s))
      0
      (let ([c (string-ref s 0)])
        (+ (if (vowel? c) 1 0) (count-vowels (substring s 1))))))

(define (good-vowels? s) (>= (count-vowels s) 3))

(define (good-string? s)
  (null? (filter (lambda (bs) (string-contains? s bs)) (list "ab" "cd" "pq" "xy"))))

(define (double? s)
  (not (null? (filter (lambda (db) (string-contains? s db)) *doubles*))))

(define (part1 s) (and (good-vowels? s) (good-string? s) (double? s)))

(println (length (filter part1 *strings*)))


(define (pair? s)
  (if (< (string-length s) 4)
      #f
      (if (string-contains? (substring s 2) (substring s 0 2))
          #t
          (pair? (substring s 1)))))

(define (sandwich? s)
  (if (< (string-length s) 3)
      #f
      (if (char=? (string-ref s 0) (string-ref s 2))
          #t
          (sandwich? (substring s 1)))))

(define (part2 s) (and (pair? s) (sandwich? s)))

(println (length (filter part2 *strings*)))
       
  