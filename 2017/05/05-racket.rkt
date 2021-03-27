#lang racket
(define *program* (map string->number (string-split (file->string "05-input.txt") "\n")))
(define *part1* (list->vector *program*))
(define *part2* (list->vector *program*))

(define (offset1 x) (add1 x))
(define (offset2 x) (if (>= x 3) (sub1 x) (add1 x)))

(define (run-program prog pc cnt func)
  (let ([prev 0])
  (for ([i (in-naturals)] #:break (>= pc (vector-length prog)))
     (begin
      ;(print (list i (add1 pc) "jmp" (vector-ref prog pc)))
      ;(println prog)
      (set! prev (vector-ref prog pc))
      (vector-set! prog pc (func prev))
      (set! pc (+ pc prev)))
    (set! cnt (add1 i))) cnt))

(println (run-program *part1* 0 0 offset1))
(println (run-program *part2* 0 0 offset2))