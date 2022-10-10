import random

# Maximum lines to bet on
MAX_LINES = 3
# Maximum and minimum betting amounts for each line
MAX_BET = 100
MIN_BET = 1
# Total numbers of rows and columns to be played on
ROWS = 3
COLUMNS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 3,
    "D": 5
}

symbol_value = {
    "A": 100,
    "B": 20,
    "C": 20,
    "D": 5
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
        amount = input("Your deposit amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ") :")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 1-3")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        bet_amount = input(f"Enter the amount you want to bet on each line (${MIN_BET}-${MAX_BET}): ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number.")
    return bet_amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You can't bet more than your balance. Your balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is {bet * lines}")
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"On lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        if balance == 0:
            print("Sorry but you lost")
            break
        else:
            print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")


main()

