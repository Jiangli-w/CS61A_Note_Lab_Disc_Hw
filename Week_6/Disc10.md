# Disc 10: Scheme, Scheme Lists

## Questions

### 3.1

What would Scheme display?

`scm> (define a (+ 1 2))`

> a

`scm> a`

> 3

`(define b (+ (* 3 3) (* 4 4)))`

> b

`scm> (+ a b)`

> 28

`scm> (= (modulo 10 3) (quotient 5 3))`

> #t

`scm> (even? (+ (- (* 5 4) 3) 2))`

> #f

### 4.1

What would Scheme display?

`scm> (if (or #t (/ 1 0)) 1 (/ 1 0))`

> 1

`scm> (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))`

> 10

`scm> ((if (< 4 3) + -) 4 100)`

> -96

`scm> (if 0 1 2)`

> 1

Write a function that returns the factorial of a number

```scm
(define (factorial x)
    (if (= x 0) 
        1
        (* x (factorial (- x 1)))
    )
)
```

### 4.2

Write a function that returns the n th Fibonacci number.

```scm
(define (fib n)
    (if (< n 2)
        n
        (+ (fib (- n 1)) (fib (- n 2)))
    )
)
```

### 5.1

Write a function which takes two lists and concatenates them.

Notice that simply calling (cons a b) would not work because it will create a deep list. Do not call the builtin procedure append, which does the same thing as my-append.

```scheme
(define (my-append a b)
    (if (null? a)
        b
        (cons (car a) (my-append (cdr a) b))
    )
)
```

### 5.2

Write a Scheme function that, when given an element, a list, and an index, inserts the element into the list at that index.

```scm
(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)
```

### 5.3

Write a Scheme function that, when given a list, such as (1 2 3 4), duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4)).

```scm
(define (duplicate lst)
    (if (null? lst) 
        lst
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)
```
