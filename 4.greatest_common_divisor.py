def greatest_common_divisor(num1, num2):

    divisors1 = set([i for i in range(1, num1+1) if num1 % i == 0])
    divisors2 = set([j for j in range(1, num2+1) if num2 % j == 0])
    return max(divisors1.intersection(divisors2))
    # We find the divisors of each given number with list comprehension, we convert them to sets, get their
    # intersection, and finally take the max value among the result of their intersection.


print(greatest_common_divisor(15, 25))