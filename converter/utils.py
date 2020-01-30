def numConverter(num):
    numArr = [int(x) for x in str(num)]
    print(numArr)
    return {
        'input': num,
        'status': 'ok',
        'value': str(num)
    }