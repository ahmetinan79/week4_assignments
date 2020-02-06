def counter(text):

    # We use list comprehension with isupper and islower to split lower and upper letters into two lists.
    s_upper = [i for i in text if i.isupper()]
    s_lower = [i for i in text if i.islower()]
    return f"smaller letter: {len(s_upper)}\nupper letter: {len(s_lower)}"
    # We find the number of lower and upper letters with len function.


print(counter("asdASD"))