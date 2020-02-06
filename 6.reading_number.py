def reading_number(number):

    # We define three dictionaries for the reading of numbers based on the first and second digits.
    first_digit = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
                   '8': 'Eight', '9': 'Nine'}
    ten_nineteen = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen',
                    '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
    twenty_ninety = {"2": 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy',
                     '8': 'Eighty', '9': 'Ninety'}

    number = str(number)  # We convert the number into an integer to index the digits.

    if len(number) == 2:  # If the number has two digits, it is good to go.
        if 10 <= int(number) <= 19:  # If the number is in between 10-19, we use the ten_nineteen dictionary.
            return ten_nineteen[number]
        elif number[1] == '0':  # If the first digit ends with 0, we use twenty_ninety dictionary.
            return twenty_ninety[number[0]]
        else:  # If the number is higher than 19 and first digit is not zero, we use two dictionaries together.
            return f"{twenty_ninety[number[0]]} {first_digit[number[1]]}"
    return 'Please enter a two-digit number'  # We warn the user, if the number different than a two-digit number.


print(reading_number(28))

