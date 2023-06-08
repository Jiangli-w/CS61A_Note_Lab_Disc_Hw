# Week_4

## Mon:Mutable Functions

A Function with Behavior That Varies Over Time

### The Effect of Nonlocal Statements

> nonlocal \<name>

**Effect:** &nbsp;Future assignments to that name change its pre-existing binding in the **first non-local frame** of the current environment in which that name is bound.

**From the python 3 language referrnce:**

Names listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope.

Names listed in a nonlocal statement must not collide with pre-existing bindings in the local scope.

```py
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return '麻蛋，自己有多少钱心里没点B数？'
        balance = balance - amount
        return balance
    return withdraw
```

### Referrntial Transparency, Lost

* Expressions are **referentially transparent** if substituting an expression with its value does not change the meaning of program.
* Mutation operations violate the condition of referential transparency because they do more than just return a value; **they change the environment.**

```py
def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

a = f(1)
b = a(2)
```

```py
>>> tatol = b(3) + b(4) 
>>> tatol 
22
```

or

```py
>>> tatol = 10 + b(4) 
>>> tatol 
21
```

## Wed:Iterators & Generators

### Iterators

A container can provide an iterator that provides access to its elements in some order.

> **iter**(iterable): Return an iterator over the elements of an iterable value </br> </br>
> **next**(iterator): Return the next element in an iterator

### Dictionary Iteration

#### Views of a Dictionary

An iterable value is any value that can be passed to **iter** to produce an iterator

An iterator is returned from **iter** and can be passed to **next**; all iterators are mutable

A dictionary, its keys, its values, and its items are all iterable values

* The order of items in a dictionary is the order in which they were added (Python 3.6+)
* Historically, items appeared in an arbitrary order (Python 3.5 and earlier)

```py
>>> d = {'one':1, 'two':2, 'three':3}
>>> d['zero'] = 0
>>> k = iter(d.keys())  # or iter(d)
>>> v = iter(d.values())
>>> i = iter(d.items())
>>> next(k), next(v), next(i)
('one', 1, ('one': 1))
>>> next(k), next(v), next(i)
('two', 2, ('two', 2))
>>> next(k), next(v), next(i)
('three', 3, ('three', 3))
>>> next(k), next(v), next(i)
('zero', 0, ('zero', 0))
```

### Built-in Iterator

Many built-in Python sequence operators that compute results lazily

> **map**(func, iterable): &nbsp; Iterate over func(x) for x in iterable </br>
> **filter**(func, iterable): &nbsp; Iterate over x in iterable if func(x) </br>
> **zip**(first_iter, second_iter): &nbsp; Iterate over co-indexed (x, y) pairs </br>
> **reversed**(sequence): &nbsp; Iterate over x in a sequence in reverse order

To view the contents of an iterator, place the resulting elements into a container

> **list**(iterable): &nbsp; Create a list containing all x in iterable </br>
> **tuple**(iterable): &nbsp; Create a tuple containing all x in iterable </br>
> **sorted**(iterable): &nbsp; Create a sorted list containing x in iterable

### Generators

#### Generators and Generator Functions

```py
>>> def plus_minus(x):
...     yield x
...     yield -x

>>> t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3
>>> t
<generator object plus_minus ...>
```

A *generator function* is a function that **yield**s values instead of **return**ing them

A normal function **return**s once; a *generator function* can **yield** multiple times

A *generator* is an iterator created automatically by calling a *generator function*

When a *generator function* is called, it returns a *generator* that iterates over its yields

### Generators & Iterators

#### Generators can Yield from Iterators

A **yield from** statement yields all values from an iterator or iterable (Python 3.3)

```py
>>> def a_then_b(a, b):
...    for x in a:
...        yield x
...    for x in b:
...        yield x

>>> list(a_then_b([3, 4], [5, 6]))
[3, 4, 5, 6]

>>> def a_then_b(a, b):
...     yield from a
...     yield from b

>>> list(a_then_b([3, 4], [5, 6]))
[3, 4, 5, 6]
```

```py
>>> def countdown(k):
...     if k > 0:
...         yield k
...         yield from countdown(k-1)

>>> list(countdown(5))
[5, 4, 3, 2, 1]
```

```py
>>> def prefixes(s):
...     if s:
...     yield from prefixe(s[:-1])
...     yield s

>>> list(prefixes('both'))
['b', 'bo', 'bot', 'both']
```
