def prime_number(number):

    for num in range(3, number):  # We use a for loop in range between 3 and the number.
        if number % num == 0:  # If the number can be divided by any number, we break the loop at this point.
            return f"{number} is a not prime number."
        break
    return f"{number} is a prime number."  # If the number cannot be divided by any number, then it is a prime number.


print(prime_number(123))