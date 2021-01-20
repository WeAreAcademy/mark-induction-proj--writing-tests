---
module: mark-induction

level: 2

methods:
  - team
  - pair
  - solo

tags:
  - wip
---

# Writing Tests

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>

> This is part of Academy's [technical curriculum for **The Mark**](https://github.com/WeAreAcademy/curriculum-mark). All parts of that curriculum, including this project, are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

We're going to look at writing tests for code.

## Learning Outcomes

- Write tests for existing code
- Run Python tests with pytest
- Debug failings tests run with pytest

## Exercise 0: Installing and running tests with `pytest`

> 🎯 **Success criterion:** You are able to run `pytest` in your terminal and see test results as expected.

We'll be writing tests using the `pytest` framework.

From the [`pytest` docs](https://docs.pytest.org/en/stable/getting-started.html), you should:

- Read and follow _Install `pytest`_
- Read and follow _Create your first test_

We suggest that you do this within an `exercise-0` subdirectory of this repository. (This means you can easily run all tests relevant _only_ to Exercise 0 by `cd`ing into `exercise-0` and running `pytest` within that directory.)

Once you have done this, you should see the below (as the `pytest` docs say):

```bash
================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_sample.py::test_answer - assert 4 == 5
============================ 1 failed in 0.12s =============================
```

Broadly, tests can fail because of two common reasons:

1. The function which is being tested has been incorrectly implemented; or
2. The function has a correct implementation, but the test is erroneously specified.

In this case, we can't really tell, because it's unclear what `func` is meant to do.

So, replace `test_sample.py` with the following:

```py
def add_one(n):
    return n + 1

def add_five(n):
    return n + 5

def double(n):
    return n * n

def test_add_one():
    assert add_one(11) == 10

def test_add_five():
    assert add_five(11) == 16

def test_double():
    assert double(11) == 22
```

Before you run `pytest`, predict: how many tests should be failing, and why?

Now, see if you can get all the tests passing by making appropriate changes to the code:

- if the test is correct, fix the function;
- if the function is correct, fix the test.

## Exercise 1: Refactoring some existing code

> 🎯 **Success criterion:** a refactored version of the exercise 1 code which still passes the existing tests

One of the great things about tests is that they help us refactor code with confidence that you're not unknowingly breaking anything.

(In the last exercise, [Game of Refactoring](https://github.com/WeAreAcademy/mark-induction-proj--game-of-refactoring), what was it like to try to refactor without knowing whether or not things were still behaving as expected?)

Firstly, confirm that the Exercise 1 tests pass by `cd`ing into `exercise-1` and running `pytest`.

Now, inspect the code at `exercise-1/main.py`. It's not great - there have been a couple of TODOs left for us to, um, do.

(`describe_number` in particular looks pretty hard to read and reason about. It miraculously seems to be doing the job, since the tests are passing, but we should try to improve it...)

For `hello_world` and `greet`, see if you can refactor following the suggestion into the TODO note.

When you get to `describe_number`, you'll see it's a bit of a mess. See if you can use things which you've already seen before on identifying code smells and using refactoring techniques.

There are two ways you might find useful to approach the refactor:

1. **Small changes.** It can be overwhelming to work through some foreign code. Try to make one small improvement. (Then another, and another...)
2. **Start from scratch.** _Sometimes_ it can be easier to rewrite a function from a blank slate.

## Exercise 2: Commentary and reflection

**Success criterion:** documented reflections.
