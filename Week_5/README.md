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

Every object that is an instance of a user-defined class has a unique identity:

```py
>>> a = Account('Jim')
>>> b = Account('Jack') # Every call to Account creates a new Account instance. There is only one Account class.
>>> a.balance
0
>>> b.holder
'Jack'
```

Identity operators "is" and "is not" test if two expressions evaluate to the same object:

```py
>>> a is a
True
>>> a is not b
True
```

Binding an object to a new name using assignment does not create a new object:

```py
>>> c = a
>>> c is a
True
```

### Methods

Methods are defined in the suite of a class statement

```py
class Account:
  def __init__(self, account_holder):
    self.balance = 0
    self.holder = account_holder

  def deposit(self, amount):
    self.balance = self.balance + amount

  def withdraw(self, amount):
    if amount > self.balance:
      return  '自己有多少钱心里没点B数？'
    self.balance = self.balance - amount
    return self.balance
```

These def statements create function objects as always, but their names are bound as attributes of the class.

#### Invoking Methods

All invoked methods have access to the object via the self parameter, and so they can all access and manipulate the object's state.

```py
class Account
  def deposit (self, amount): # Defined with two arguments
    self.balance = self.balance + amount 
    return self.balance
```

Dot notation automatically supplies the first argument to a method.

```py
>>> tom_account = Account('TOm')
>>> tom_account.deposit(100) # Inboked with one argument
100
```

#### Dot Expressions

Objects receive messages via dot notation.

Dot notation accesses attributes of the **instance** or its **class**.

```<expression>, <name>```

The `<expression>` can be any valid Pytho expression.

The `<name>` must be a simple name

Evaluates to the value of the attribute looked up by `<name>` in the object
that is the value of the `<expression>`.

```py
>>> tom_account.deposit(10)
110
```

### Attributes

#### Accessing Attributes

Using getattr, we can look up an attribute using a string

```py
>>> getattr(tom_account, 'balance')
10
>>> hasattr(tom_account, 'deposit')
True
```

getattr and dot expressions look up a name in the same way

Looking up an attribute name in an object may return: 

* One of the its instance attributes, **or**
* One of the attributes of its class

#### Methods and Functions

Python distinguishes between:

* Functions, which we have been creating since the beginning of the course,
* Bound methods, which couple together a function and the object on which that method will be invoked.

> Object + Function = Bound Methon

```py
>>> type(Account.deposit)
<class 'function'>
>>> type(tom_account.deposit)
<class 'method'>

>>> Account.deposit(tom_account, 1001)
1011
>>> tom_account.deposit(1000)
2011
```

#### Looking Up Attributes by Name

`<expression>, <name>`

To evaluate a dot expression:

1. Evaluate the `<expression>` to the left of the dot, which yields the object of the dot expression.
2. `<name>` is matched against the instance attributes of that object; **if an attribute with that name exists,** its value is returned.
3. If not, `<name>` is looked up in the class, which yields a class attribute value.
4. That value is returned **unless it is a function,** in which case a *bound method* is returned instead.

#### Class Attributes

Class attributes are "shared" across all instances of a class because they are attributes of the class, not the instance.

```py
class Account:
  interest = 0.02   # A class attribute

  def __init__(self, account_holder):
    self.balance = 0
    self.holder = account_holder

  # Addittional methods would be defined here
```

```py
>>> tom_account = Account('Tom')
>>> jim_account = Account('Jim')
>>> tom_account.interest # interest is not part of the instance that was somehow copied from the class!
0.02
>>> jim_account.interest
0.02
```

### Examples: Object

Instance attributes are found before class attributes; class attributes are inherited

```py
class Worker:
  greeting = 'Sir'

  def __init__(self):
    self.elf = Worker
  
  def work(self):
    return self.greeting + ', I work'

  def __repr__(self):
    return Bourgeoisie.greeting

class Bourgeoisie(Worker):
  greeting = 'Peon'
  
  def work(self):
    print(Worker.work(self))
    return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
```

```py
>>> Worker().work()
'Sir, I work'

>>> jack
Peon

>>> jack.work()
'Maam, I work'

>>> jack.work()
'Maam, I work'

>>> john.work()
Peon, I work
'I gather wealth'

john.elf.work(john)
'Peon, I work'
```
