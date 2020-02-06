def exact_divisor(number):

    return [i for i in range(1, number + 1) if number % i == 0]
    # We use list comprehension recording numbers that can divide the given number.


print(*exact_divisor(12))