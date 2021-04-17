#lang racket

; HA: why yes, this is very non-functional programming.

(define-syntax-rule (while condition body ...)
  (let loop ()
    (when condition
      body ...
      (loop))))

(define *program*
  (list->vector 
    (map (λ (s) (let ([xs (string-split s " ")])
                (list (car xs) (string->number (cadr xs)))))
       (string-split (file->string "08-input.txt") "\n"))))

(define (run program)
  (let ([pc 0]
        [acc 0]
        [instr-cnt (make-vector (vector-length program) 0)]
        [dup #f])
    (while (and (>= pc 0) (< pc (vector-length program)) (not dup))
           (let* ([instr (vector-ref program pc)]
                  [op (car instr)]
                  [operand (cadr instr)])
             (begin
               (vector-set! instr-cnt pc 1)
               (cond ((string=? op "acc") (begin (set! acc (+ acc operand)) (set! pc (add1 pc))))
                     ((string=? op "nop") (set! pc (add1 pc)))
                     ((string=? op "jmp") (set! pc (+ pc operand)))
                     (else (error "Unknown opcode")))
               (if (and (< pc (vector-length program)) (= 1 (vector-ref instr-cnt pc)))
                   (set! dup #t)
                   #f))))
   (list dup acc)))
                                          
(println (cadr (run *program*)))

(define (nop-or-jmp? line) (or (string=? (car line) "nop") (string=? (car line) "jmp")))

(define (toggle statement)
  (if (string=? (car statement) "jmp") (cons "nop" (cdr statement)) (cons "jmp" (cdr statement))))

(define (toggle-line program line-no)
  (for/vector ([i (range 0 (vector-length program))])
    (if (= i line-no)
        (toggle (vector-ref program i))
        (vector-ref program i))))

(define (part2)
  (let ([acc null])
    (for/first ([i (range 0 (vector-length *program*))]
      #:when (if (nop-or-jmp? (vector-ref *program* i))
                 (begin
                   (set! acc (run (toggle-line *program* i)))
                   (not (car acc)))
                 #f))
      (cadr acc))))

(println (part2))
                     
                   