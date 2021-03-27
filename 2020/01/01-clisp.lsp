; I haven't touched lisp since college. This is bad and needs refactoring!

(defun read-lines (filename)
  (with-open-file (in filename)
    (loop for line = (read-line in nil nil)
      while line
      collect line)))

(defun sum (x) (if (listp x) (reduce #'+ x) x))
(defun mul (x) (if (listp x) (reduce #'* x) x))

(defparameter *numbers* (mapcar #'parse-integer (read-lines "01-input.txt")))
(defun solution (x) (member (- 2020 (sum x)) *numbers*))

(defun pair-with (elem lst)
  (mapcar (lambda (a) (list elem a)) lst))

(defun uniq-pairs (lst)
  (mapcon (lambda (rest) (pair-with (car rest) (cdr rest)))
          (remove-duplicates lst)))

(defparameter *part1* (mul (remove-if-not #'solution *numbers*)))
(defparameter *part2* 
  (let ((b (car (remove-if-not #'solution (uniq-pairs *numbers*)))))
    (* (- 2020 (sum b)) (mul b))))

(print *part1*)         
(print *part2*)         


