#lang racket

(define (parse-part s)
  (let ([parts (string-split s)])
    (cons (cadr parts) (string->number (car parts)))))

(define *requirements* (map (λ (line)
                              (let* ([lst (reverse (string-split line " => "))]
                                     [hd (parse-part (car lst))]
                                     [tl (map parse-part (string-split (last lst) ", "))])
                                (cons hd tl)))
                            (file->lines "14-input.txt")))

(define (divmod a b) (cons (floor (/ a b)) (modulo a b)))

(define (solve comp amount rest)
  (if (string=? comp "ORE")
      amount
      (let* ([match (for/first ([p *requirements*] #:when (string=? (caar p) comp)) p)]
             [sources (cdr match)]
             [numreq (cdar match)]
             [already-made (if (hash-has-key? rest comp) (hash-ref rest comp) 0)]
             [d-m (divmod (- amount already-made) numreq)]
             [div (car d-m)]
             [mod (cdr d-m)]
             [new-amount (if (zero? mod) div (add1 div))])
        (hash-set! rest comp (if (zero? mod) 0 (- numreq mod)))
        (apply +
               (map (λ (n source) (solve source (* n new-amount) rest))
                    (map cdr sources)
                    (map car sources))))))
    
(solve "FUEL" 1 (make-hash))
