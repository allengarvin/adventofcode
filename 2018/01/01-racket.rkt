#lang racket
(require dyoo-while-loop)

(define *inputs* (map string->number (string-split (file->string "01-input.txt") "\n")))

(define (part2 xs)
  (let ([original xs]
        [memo (make-hash)])
    (define (helper ys acc)
      (if (null? ys)
          (helper original acc)
          (let ([n (+ acc (car ys))])
            (if (hash-ref memo n #f)
                n
                (begin
                  (hash-set! memo acc #t)
                  (helper (cdr ys) n))))))
    (helper xs 0)))

(println (apply + *inputs*))
(println (part2 *inputs*))
