from .constants import ONES, TENS, TEENS, LEVELS

def numConverter(number):
    word = ""
    num = reversed(str(number))
    number = ""
    for x in num:
        number += x
    del num
    if len(number) % 3 == 1: number += "0"
    x = 0
    for digit in number:
        if x % 3 == 0:
            word = LEVELS[int(x / 3)] + ", " + word
            n = int(digit)
        elif x % 3 == 1:
            if digit == "1":
                num = TEENS[n]
            else:
                num = TENS[int(digit)]
                if n:
                    if num:
                        num += "-" + ONES[n]
                    else:
                        num = ONES[n]
            word = num + " " + word
        elif x % 3 == 2:
            if digit != "0":
                word = ONES[int(digit)] + " hundred " + word
        x += 1
    return word.strip(", ")

def validateNum(num):
    try:
        number = int(num)
    except:
        return False
    return True