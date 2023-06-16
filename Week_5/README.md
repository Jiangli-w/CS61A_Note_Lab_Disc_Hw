# Week_5

## Mon: Objects

### Object-Oriented Programming

A method for organizing modular programs

* Abstraction barriers
* Bundling together information and related behavior

A metaphor for computation using distributed state

* Each *object* has own local state.
* Each object also knows how to manage its own local state, based on method calls.
* Method calls are messages passed between objects.
* Several objects may all be instances of a common type.
* Different types may relate to each other.

Specialized syntax & vocabulary to support this metaphor

#### Classes

A class serves as a template for its instances

> **Idea:** All bank accounts have a balance and an account holder; the Account class should add those attributes to each newly created instance.

```py
>>> a = Account('Jim')
>>> a.holder
'Jim'
>>> a.balance
```

> **Idea:** All bank accounts should have "withdraw" and "deposit" behaviors that all work in the same way. -->

```py
>>> a.deposit(15)
15
>>> a.withdraw(10)
5
>>> a.balance
5
>>> a.withdraw(10)
'Insufficient funds'
```

> **Better idea:** All bank accounts share a "withdraw" method and a "deposit" method.

### Class Statements

#### The Class Statement

```py
class <name>:
    <suite> # The suite is executed when the class statement is executed
```

A class statement creates a new class and binds that class to `<name>` in the first frame of the current environment.

Assignment & def statements in `<suite>` create attributes of the class (not names in frames)

```py
>>> class Clown:
...     nose = 'big and red'
...     def dance():
...     return 'No thanks'
...
>>> Clown.nose
'big and red'
>>> Clown.dance()
'No thanks'
>>> Clown
<class '__main__.Clown'>
```

#### Object Construction

> **Idea:** All bank accounts have a balance and an account holder; the Account class should add those attributes to each of its instances

```py
>>> a = Account('Jim')
>>> a.holder
'Jim'
>>> a.balance
0
```

When a class is called:

  1. A new instance of that is created: balance: 0 &nbsp;&nbsp; holder: 'Jim'
  2. The `__init__` method of the class is called with the new object as its first argument (named `self`), along with any additional arguments provided in the call expression.

```py
class Account:
    # __init__ is called a contructor
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
```

#### Object Identity

Every object