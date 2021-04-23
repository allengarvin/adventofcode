#lang racket

(define *molecule* (string-trim (file->string "05-input.txt")))

(define (reduce f xs) (and (not (empty? xs)) (foldl f (first xs) (rest xs))))

(define *chemicals*
  (map list->string
       (reduce append (for/list ([i (range 97 123)])
                        (let* ([a (list (integer->char i) (integer->char (- i 32)))]
                               [b (reverse a)])
                          (list a b))))))

(define (react-out molecule)
  (let* ([mole molecule]
         [newmole (for/last ([i *chemicals*])
                    (set! mole (string-replace mole i ""))
                    mole)])
    (if (string=? newmole molecule) mole (react-out mole))))

(println (string-length (react-out *molecule*)))

(define (integer->string i) (list->string (list (integer->char i))))
(define (eliminate-char s c) (string-replace (string-replace s (integer->string c) "") (integer->string (- c 32)) ""))

(println (apply min (for/list ([i (range 97 123)])
                      (string-length (react-out (eliminate-char *molecule* i))))))
           
         
    