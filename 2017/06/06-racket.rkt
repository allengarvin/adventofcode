#lang racket

(define-syntax-rule (while condition body ...)
  (let loop ()
    (when condition
      body ...
      (loop))))

(define *banks* (list->vector (map string->number (string-split (string-trim (file->string "06-input.txt"))))))

(define (vector-max vs)
  (if (zero? (vector-length vs))
      #f
      (let ([maximum (vector-ref vs 0)])
        (for ([i (range 0 (vector-length vs))])
          (set! maximum (max maximum (vector-ref vs i))))
        maximum)))

(define (vector-index vs n)
  (if (zero? (vector-length vs))
      #f
      (for/first ([i (range 0 (vector-length vs))] #:when (= (vector-ref vs i) n))
        i)))

(define (redistribute original-memory)
  (let ([memory (make-vector 16)])
    (vector-copy! memory 0 original-memory)
    (define (distribute n where)
      (if (zero? n)
          memory
          (let ([mod (modulo where (vector-length memory))])
            (vector-set! memory mod (add1 (vector-ref memory mod)))
            (distribute (sub1 n) (add1 where)))))
    (let* ([ndx (vector-index memory (vector-max memory))]
           [bank (vector-ref memory ndx)])
      (vector-set! memory ndx 0)
      (distribute bank (add1 ndx)))))

(define (cycle banks)
  (let ([states (list->mutable-set null)])
    (while (not (set-member? states banks))
           (set-add! states banks)
           (set! banks (redistribute banks)))
    (list banks (set-count states))))

(define *part1* (cycle *banks*))

(println (last *part1*))
(println (last (cycle (car *part1*))))
