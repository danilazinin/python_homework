import fractions


def sum_and_mult():
    a = input('Введите первую дробь: ')
    b = input('Введите вторую дробь: ')

    saved_numer_a = a_numerator = int(a[:a.find('/')])
    a_denominator = int(a[a.find('/') + 1:])
    saved_numer_b = b_numerator = int(b[:b.find('/')])
    b_denominator = int(b[b.find('/') + 1:])

    if a_denominator % b_denominator == 0 or b_denominator % a_denominator == 0:
        if a_denominator < b_denominator:
            a_numerator *= (b_denominator // a_denominator)
        else:
            b_numerator *= (a_denominator // b_denominator)
        sum_numer = a_numerator + b_numerator
        sum_denom = max(a_denominator, b_denominator)
        print(fractions.Fraction(sum_numer, sum_denom), end=' ')
    else:
        sum_numer = a_numerator * b_denominator + b_numerator * a_denominator
        sum_denom = a_denominator * b_denominator
        print(fractions.Fraction(sum_numer, sum_denom), end=' ')
    mult_numer = saved_numer_a * saved_numer_b
    mult_denom = a_denominator * b_denominator
    print(fractions.Fraction(mult_numer, mult_denom))