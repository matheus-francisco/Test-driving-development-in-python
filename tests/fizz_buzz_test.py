from functions.fizz_buzz import check_fizz_buzz

""" Use cases

- Can I call FizzBuzz
- Get "1" when I pass in 1
- Get "2" when I pass in 2
- Get "Fizz" when I pass in 3
- Get "Buzz" when I pass in 5
- Get "Fizz" when I pass in 6 (a multiple of 3)
- Get "Buzz" when I pass in 10 ( a multiple of 5 )
- Get "FizzBuzz" when I pass in 15 (a multiple of 3 and 5)
"""


def test_return_1_with_1_passed_in():
    check_fizz_buzz(1, "1")


def test_returns_2_with_passed_in():
    check_fizz_buzz(2, "2")


def test_return_fizz_with_3_passed_in():
    check_fizz_buzz(3, "Fizz")


def test_return_buzz_with_5_passed_in():
    check_fizz_buzz(5, "Buzz")


def test_returns_fizz_with_6_passed_in():
    check_fizz_buzz(6, "Fizz")


def test_returns_buzz_with_10_passed_in():
    check_fizz_buzz(10, "Buzz")


def test_return_fizbuzz_with_15_passed_in():
    check_fizz_buzz(15, "FizzBuzz")
