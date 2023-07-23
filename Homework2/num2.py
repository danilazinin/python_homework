num = 123
save_num = 123
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

print(res[::-1], hex(save_num))