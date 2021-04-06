#lang racket

(define *moves* (map string->list (string-split (file->string "02-input.txt") "\n")))
(define *keyboard1*
        (list (cons 0 "1") (cons 1 "2") (cons 2 "3")
              (cons 0+1i "4") (cons 1+1i "5") (cons 2+1i "6")
              (cons 0+2i "7") (cons 1+2i "8") (cons 2+2i "9")))
(define *keyboard2*
        (list (cons 2 "1")
              (cons 1+1i "2") (cons 2+1i "3") (cons 3+1i "4")
              (cons 0+2i "5") (cons 1+2i "6") (cons 2+2i "7") (cons 3+2i "8") (cons 4+2i "9")
              (cons 1+3i "A") (cons 2+3i "B") (cons 3+3i "C")
              (cons 2+4i "D")))
(define *pos1* 1+1i)
(define *pos2* 2+2i)

(define (move dir pos)
  (cond [(char=? dir #\U) (- pos 0+1i)]
        [(char=? dir #\L) (- pos 1)]
        [(char=? dir #\D) (+ pos 0+1i)]
        [(char=? dir #\R) (+ pos 1)]))

(define (follow xs pos keyboard)
  (if (null? xs)
      pos
      (let* ([mv (move (car xs) pos)])
        (if (assoc mv keyboard)
            (follow (cdr xs) mv keyboard)
            (follow (cdr xs) pos keyboard)))))

(define (solve start moves keyboard)
  (apply string-append
    (let ([pos start])
      (map (λ (line-of-moves)
             (let ([final (follow line-of-moves pos keyboard)])
               (begin
                 (set! pos final)
                 (cdr (assoc final keyboard))))) moves))))

(displayln (solve 1+1i *moves* *keyboard1*))
(displayln (solve 2+2i *moves* *keyboard2*))