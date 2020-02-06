def perfect_number(number):

    perfect_numbers = []  # We define an empty list to record perfect numbers within the given range.

    for i in range(1, number):  # We use a for loop to find and record the perfect numbers in the given range.
        divisors = [j for j in range(1, i) if i % j == 0]  # We use list comprehension to find divisors of each number.
        if i == sum(divisors):  # If sum of the divisors of a number is equal to the number, we add it to the list.
            perfect_numbers.append(sum(divisors))
    return perfect_numbers


print(*perfect_number(1000))