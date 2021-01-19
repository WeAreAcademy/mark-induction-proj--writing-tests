---
module: mark-induction

level: 1

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

We suggest that you do this within an `exercise-0` subdirectory of this repository.

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

## Exercise 2: Refactoring an existing solution

> 🎯 **Success criterion:** a refactored version of the sample solution which removes identified code smells

Now you've been through the existing code, it's time to refactor it.

### Refactoring techniques

- [Consolidate Conditional Expression](https://sourcemaking.com/refactoring/consolidate-conditional-expression)
- [Decompose Conditional](https://sourcemaking.com/refactoring/decompose-conditional)
- [Extract Method](https://sourcemaking.com/refactoring/extract-method)
- [Extract Variable](https://sourcemaking.com/refactoring/extract-variable)

## Exercise 3: Sample refactoring investigation

The folder `refactored` has a sample refactoring of `original/main.py`.

Read through it with the same lens of above:

1. Quick big picture
2. Clarity of intent
3. Ease of navigation

What are the things which are better in this solution than the original one?

## Exercise 4: Check your understanding

> 🎯 **Success criterion:** a conversation with a Faculty member and amended comments.

Talk to a member of Faculty about your refactored solution and your understanding of code smells and refactoring techniques.

Amend your notes for any important points that come out of the conversation.

## Exercise 5: Commentary and reflection

**Success criterion:** documented reflections.
