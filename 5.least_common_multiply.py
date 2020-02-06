def least_common_multiply(num1,num2):

    min_multiply = []

    divisors1 = ([i for i in range(1, num1+1) if num1 % i == 0])  # We find the divisors of the first number.
    divisors2 = ([j for j in range(1, num2+1) if num2 % j == 0])  # We find the divisors of the second number.

    # We find the all possible multiplies of each number by multiplying the numbers with the other number's divisors.
    multiply1 = [m*num1 for m in divisors2]
    multiply2 = [n*num2 for n in divisors1]

    return min(set(multiply1).intersection(set(multiply2)))
    # We take the intersection of two lists as sets and use min function to find the least common multiply.


print(least_common_multiply(3, 4))