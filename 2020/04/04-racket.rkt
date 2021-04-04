#lang racket

(define (attr-pair s)
  (let ([s (string-split s ":")])
    (cons (car s) (cadr s))))

(define *records* (map (λ (s)
                         (map attr-pair (string-split (string-trim (string-replace s "\n" " ")) " ")))
                       (string-split (file->string "04-input.txt") "\n\n")))

(define (is-digit? s) (regexp-match #px"^\\d+$" s))
(define (is-hex? s) (regexp-match #px"^[0-9a-f]+$" s))

(define (test-height s)
  (let ([re (regexp-match #px"^(\\d+)([ic][nm])" s)])
    (if (not re)
        #f
        (let ([val (string->number (cadr re))]
              [unit (caddr re)])
          (or (and (string=? "in" unit) (<= 59 val 76))
              (and (string=? "cm" unit) (<= 150 val 193)))))))
    
(define *testers*
  (list
   (cons "byr" (λ (s) (let ([n (string->number s)]) (<= 1920 n 2002))))
   (cons "iyr" (λ (s) (let ([n (string->number s)]) (<= 2010 n 2020))))
   (cons "eyr" (λ (s) (let ([n (string->number s)]) (<= 2020 n 2030))))
   (cons "hcl" (λ (s) (and (= (string-length s) 7) (char=? #\# (string-ref s 0)) (is-hex? (substring s 1 7)))))
   (cons "cid" (λ (s) #t))
   (cons "hgt" test-height)
   (cons "ecl" (λ (s) (member s (list "amb" "blu" "brn" "gry" "grn" "hzl" "oth"))))
   (cons "pid" (λ (s) (and (= (string-length s) 9) (is-digit? s))))))

(define *part1*
  (filter (λ (xs) (or (= (length xs) 8)
                      (and (= (length xs) 7) (not (assoc "cid" xs))))) *records*))

(define (test-part2 xs)
  (let* ([field (car xs)]
         [val (cdr xs)]
         [p (assoc (car xs) *testers*)])
    (cond [(not p) #f]
          [else ((cdr p) val)])))

(define *part2* (filter (λ (xs) (andmap identity (map test-part2 xs))) *part1*))

(println (length *part1*))
(println (length *part2*))
