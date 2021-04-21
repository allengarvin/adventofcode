#lang racket

(define *presents* ((compose string->number string-trim file->string) "20-input.txt"))

(define (solve n part2?)
  (define (part2-limit x lim)
    (if (< (* x 50) lim)
        (add1 (* x 50))
        lim))
  (let* ([limit (quotient n 20)]
         [arr (make-vector limit 0)])
    (for ([i (range 1 limit)])
      (for ([j (range i (if part2? (part2-limit i limit) limit) i)])
        (vector-set! arr j (+ (if part2? (* 11 i) (* 10 i)) (vector-ref arr j)))))
    (for/first ([i (range 1 limit)] #:when (> (vector-ref arr i) n)) i)))

(println (solve *presents* #f))
(println (solve *presents* #t))
            