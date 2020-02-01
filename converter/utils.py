from .constants import ONES, TENS, TEENS, LEVELS

def numConverter(num):
    word = ''
    list = [int(x) for x in str(num)]
    r_list = list[::-1]
    if len(r_list) % 3 == 1: r_list.append(0)
    x = 0
    for digit in r_list:
        if x % 3 == 0:
            word = LEVELS[int(x / 3)] + ", " + word
            ones = digit
        elif x % 3 == 1:
            if digit == 1:
                num = TEENS[ones]
            else:
                num = TENS[digit]
                if ones:
                    if num:
                        num += "-" + ONES[ones]
                    else:
                        num = ONES[ones]
            word = num + " " + word
        elif x % 3 == 2:
            if digit != 0:
                word = ONES[digit] + " hundred " + word
        x += 1
    return word.strip(", ")

def validateNum(num):
    try:
        number = int(num)
    except:
        return False
    return True