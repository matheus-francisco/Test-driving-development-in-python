def fizz_buzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return (value % mod) == 0


def check_fizz_buzz(value, expected_ret_val):
    ret_val = fizz_buzz(value)
    assert ret_val == expected_ret_val
