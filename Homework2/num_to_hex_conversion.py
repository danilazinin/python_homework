def num_to_hex(num):

    if isinstance(num, (float, str)):
        raise TypeError('Value must be an integer type')

    res = ''
    letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 15: 'E', 16: 'F'}
    HEX_NUMBER = 16

    while num > 0:
        rest = num % HEX_NUMBER
        if rest >= 10:
            res += letters[rest]
        else:
            res += str(rest)
        num //= HEX_NUMBER
    return res[::-1]