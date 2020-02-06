def alphabetical_order():

    text = input("Please enter words by putting - in between: ")  # We take input from the user.
    words_list = [word for word in text.split('-')]  # We use list comprehension to make list of words.
    words_list.sort()  # We sort the words in alphabetical order.
    print(*words_list, sep="-")  # We print the sorted words with '-' in between them.


alphabetical_order()