#lang racket
(require data/monad data/applicative)
(require megaparsack megaparsack/text)

(define rules/p
  (do [a <- integer/p]
      (char/p #\-)
      [b <- integer/p]
      space/p
      [x <- letter/p]
      (char/p #\:)
      space/p
      [passwd <- (many/p letter/p)]
      (pure (list a b x passwd))))

(define *passwords*
  (map (λ (line) (parse-result! (parse-string rules/p line)))
       (file->lines "02-input.txt")))

(define (part1 p)
  (match-define (list lower upper char passwd) p)
  (<= lower (length (filter (λ (c) (char=? c char)) passwd)) upper))

(define (part2 p)
  (match-define (list lower upper char passwd) p)
  (define (match-char n) (char=? char (list-ref passwd (- n 1))))
  (xor (match-char lower) (match-char upper)))

(println (length (filter part1 *passwords*)))
(println (length (filter part2 *passwords*)))

