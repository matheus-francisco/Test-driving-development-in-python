# Learning about Unit Testing and Test Driven Development




## Levels of Testing

* Unit Testing - Testing at the function level.
* Component Testing - Testing is at the library and compiled binary Levels
* System Testing - Tests the external interfaces of a system which is a collection of sub-systems.
* Performance Testing- Testing done at sub-system and system levels to verify timing and resource usages are acceptable.


## Unittesting specifics

* Test individual functions
* A test should be written for each test case for a function (all positive and negative test cases)
* Groups of tests can be combined into test suites for better organizations.
* Executes in the development environment rather than the production environment.
* Execution of the tests should be automated


```
# simple example
import pytest

def str_len( theStr ):
    return len(theStr)

def test_string_length():
    testStr = "1"
    result = str_len(testStr)
    assert result == ''
```

* Unit test are the first safety net for catching bugs before they get to the field.
* Unit test validate test cases for individual functions.
* They should build and run in the developer's development environment.
* Unit tests should run fast!

## What is test driven development ?

* A process where the developer takes personal responsability for the quality of their code.
* Unit tests are written before the production code.
* Don't write all the tests or production code ate once.
* Tests and production code are both written together in small bits of functionality

## Ehat are some of the benefits of tdd?

* Gives you the confidence to change the code.
* Gives you immediate feedback.
* Documents what the code is doing.
* Drives good object oriented design.

> TDD beginmomgs
> Created by Kent Beck in the 1990's as part of the Extreme Programming software development process.
> He wrote the first TDD unit testing framework in Smalltalk called Sunit.




