def pythagoras(number):

    list_sides = []  # We define a list to record the combinations that meet the Pythagoras triangle.

    for i in range(1, number):  # We use 3 for loops in a given range since we have 3 sides.
        for j in range(1, number):
            for k in range(1, number):
                if i < j and i**2 + j**2 == k**2:  # We have a condition to prevent repetitions and for Pythagoras.
                    list_sides.append((i, j, k))  # We record the combinations to our list as tuples.
    return list_sides


print(*pythagoras(100))