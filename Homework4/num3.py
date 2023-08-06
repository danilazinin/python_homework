PERCENTAGE_FOR_WITHDRAWAL = 1.5
THIRD_OPERATION_PERCENT = 3
WEALTH_TAX = 10
DEPOSIT_LIMIT = 5_000_000
MULTIPLE_AMOUNT = 50
LOWER_WITHDRAWAL_AMOUNT = 30
UPPER_WITHDRAWAL_AMOUNT = 600
deposit = 0
operations_counter = 0
transaction_lst = []


def print_menu():
    show_deposit()
    print('Выберите действие:\n1. Пополнить счет\n2. Снять\n3. Выйти')


def show_deposit():
    print(f'На счету: {deposit}')


def transaction_list_dict(name, result):
    transaction_lst.append((name, result))


def make_a_deposit():
    global operations_counter
    global deposit
    while True:
        user_deposit = input('Введите сумму для внесения на счет: ')
        if not user_deposit.isdigit():
            print('Введите число!')
            continue
        user_deposit = int(user_deposit)
        if user_deposit % MULTIPLE_AMOUNT == 0:
            if operations_counter == 3:
                deposit += deposit * THIRD_OPERATION_PERCENT / 100
                operations_counter = 0
            deposit += user_deposit
            operations_counter += 1
            if check_deposit_limit():
                deposit -= deposit * WEALTH_TAX / 100
            transaction_list_dict('Пополнение счета', user_deposit)
            break
        else:
            print('Сумма должна быть кратной 50!')


def make_a_withdrawal():
    global operations_counter
    global deposit
    while True:
        amount = input('Какую сумму хотите снять? ')
        if not amount.isdigit():
            print('Введите число!')
            continue
        amount = int(amount)
        if amount > deposit:
            print('Не достаточно средств на счёте!')
            break

        if amount % MULTIPLE_AMOUNT == 0 and LOWER_WITHDRAWAL_AMOUNT < amount < UPPER_WITHDRAWAL_AMOUNT:
            if operations_counter == 3:
                deposit += deposit * THIRD_OPERATION_PERCENT / 100
                operations_counter = 0
            deposit -= ((amount * PERCENTAGE_FOR_WITHDRAWAL / 100) + amount)
            operations_counter += 1
            if check_deposit_limit():
                deposit -= deposit * WEALTH_TAX / 100
            transaction_list_dict('Снятие со счета: ', amount)
            break
        else:
            print('Сумма должна быть не менее 30 и не более 600 у.е., а так же кратной 50')


def check_deposit_limit():
    global deposit
    if deposit > DEPOSIT_LIMIT:
        return True
    return False


while True:
    print_menu()
    user_input = input()
    if not user_input.isdigit():
        print('Введите число!')
        continue
    user_input = int(user_input)
    if user_input == 1:
        show_deposit()
        make_a_deposit()
    elif user_input == 2:
        show_deposit()
        make_a_withdrawal()
    elif user_input == 3:
        print('До свидания!')
        exit()
    else:
        print('Некорректный ввод')