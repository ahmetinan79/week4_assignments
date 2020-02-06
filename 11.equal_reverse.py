def equal_reverse(text):

    return text == text[::-1]  # We check whether the regular and reverse versions of a word are same.
    # text = "".join((text.lower().split())) This code can be used for a word or phrase with spaces and upper letters.


print(equal_reverse("tacocat"))