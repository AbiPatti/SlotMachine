# Abinash Patti
# First python project - simple slot machine game

# Constants
MAX_LINES = 3

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


# Main game function
def main():
    balance = deposit()
    lines = getNumberOfLines()

welcomeMessage()
main()