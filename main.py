# Abinash Patti
# First python project - simple slot machine game

import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Count of each symbol
symbolCount = {
    "⭐": 2,
    "🍇": 4,
    "🍒": 6,
    "🍌": 8
}

# Multiplier of each symbol 
symbolValue = {
    "⭐": 10,
    "🍇": 5,
    "🍒": 3,
    "🍌": 2
}

# Function to check winnings
def checkWinnings(columns, lines, bet, values):

    winnings = 0
    winningLines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck: # If one symbol does not match
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1) # add current line, accounting for 0-based indexing
        
    return winnings, winningLines

# Function to spin the slot machine
def getSlotMachineSpin(rows, cols, symbols):

    # Fill the allSymbols list by appending symbol
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    # Generate random symbols in the slot machine
    columns = []
    for col in range(cols):
        column = []
        currentSymbols = allSymbols[:] # making a copy of allSymbols
        for row in range(rows):
            value = random.choice(currentSymbols) # choose a random symbol
            currentSymbols.remove(value) # remove an occurance of that symbol from list
            column.append(value)

        columns.append(column)

    return columns

# Function to display the slot machine results
def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # if loop is not at the last element, print "|"
                print(column[row], end="|") # end operator to not move to next line
            else:
                print(column[row], end="") # end operator to not move to next line

        print()

# Function to welcome users to game
def welcomeMessage():
    print("Welcome to Abinash's Slot Machine!")
    print("Remember, 99% of gamblers quit before their big win!")
    print("\n" + "="*50 +"\n")

# Function to collect user deposit
def deposit():
    while True:
        amount = input("Enter amount to deposit: $")

        # Input validation - Must be a valid float
        try:
            amount = float(amount)
            # Input validation - Must be greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a number.")
    
    return amount

# Function to collect number of slot lines
def getNumberOfLines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")

        # Input validation - Must be a valid float
        try:
            lines = int(lines)
            # Input validation - Must be within lines range
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        except ValueError:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("Enter amount to bet on each line: $")

        # Input validation - Must be a valid float
        try:
            amount = float(amount)
            # Input validation - Bet must be between min and max bet
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        except ValueError:
            print("Please enter a number.")
    
    return amount

# Spin
def spin(balance):
    lines = getNumberOfLines()

    while True:
        bet = get_bet()
        totalBet = bet * lines

        # Input validation - Total bet must be less than balance
        if totalBet > balance:
            print(f"You do not have enough funds to bet that amount, your current balance is: ${balance}")
        else:
            break

    # Display bet information
    print(f"\nYou are betting ${bet} on {lines} lines. Total amount bet: ${totalBet}")

    # Spin slot machine
    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)

    # Print slot machine
    printSlotMachine(slots)

    # Display winnings
    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
    print(f"You won ${winnings}!")
    print(f"You won on lines: ", *winningLines)

    return winnings - totalBet

# Main game function
def main():
    balance = deposit()

    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or q to quit.")

        if answer.lower() == "q":
            print("\nThank you for playing Abinash's Slot Machine!")
            break

        balance += spin(balance)

    #Display final balance
    print(f"You left with ${balance}")

welcomeMessage()
main()