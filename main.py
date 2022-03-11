"""   ********* RCN Soft *********
    If decimal exists, it constructs the word for point value.
    After removing the decimal digits from the number,
    it converts digits, tens, hundreds and thousands by using the functions
    which return a string containing the number in words.
    if user enter "9876", it converts to "$NineThousand EightHundred SeventySix"
    user is  allowed only numeric characters
"""

def convertword(digit):
    num = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
           7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Ten',
           13: 'Eleven', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
           17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
           30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
           80: 'Eighty', 90: 'Ninety'}
    return num[digit]


def digit2(value):
    result = ''
    if value > 0 and value < 20:
        result += convertword(value)
    elif value > 19 and value < 100:
        division = 10 * (value // 10)
        result += convertword(division)
        remind = value % 10
        if remind != 0:
            result += convertword(remind)

    return result


def digit3(value):
    result = ''
    if value > 99 and value < 1000:
        division = value // 100
        result += convertword(division) + 'Hundred '
        remind = value % 100
        if remind != 0:
            result += digit2(remind)
    return result


def digit4(value):
    result = ''
    if value > 999 and value < 1000000:
        division = value // 1000
        if division < 100:
            result += digit2(division) + 'Thousand '
        else:
            result += digit3(division) + 'Thousand '
        remind = value % 1000
        if remind != 0:
            result += digit3(remind)
    return result


state = True
while state:
    number_str = input('Enter a number --> ')
    if not number_str.isdigit() or len(number_str) > 6:
        print('Invalid number try again')
        state = True
    else:
        state = False
    print()

number = int(number_str)
if number < 20:
    text = convertword(number)
elif number > 19 and number < 100:
    text = digit2(number)
elif number > 99 and number < 1000:
    text = digit3(number)
elif number > 999 and number < 1000000:
    text = digit4(number)
print('$ ' + text)