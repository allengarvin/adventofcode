#lang racket

(define *keys* (map string->number (file->lines "25-input.txt")))

(define (transform-1 subject key1 key2)
  (let ([val 1])
    (for/first ([cnt (in-naturals 1)]
                #:when (begin
                         (set! val (remainder (* val subject) 20201227))
                         (or (= val key1) (= val key2))))
      (list (if (= val key1) key2 key1) cnt))))

(define (transform-2 subject cnt-max)
  (let ([val 1])
    (for ([i (range cnt-max)])
      (set! val (remainder (* val subject) 20201227)))
    val))

(define *new-keys* (transform-1 7 (first *keys*) (last *keys*)))
(transform-2 (first *new-keys*) (last *new-keys*))
  
  
      