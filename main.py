# Abinash Patti
# First python project - simple slot machine game

# Function to welcome users to game
def welcomeMessage():
    print("Welcome to Abinash's Slot Machine!")
    print("Remember, 99% of gamblers quit before their big win!")

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

welcomeMessage()
deposit()