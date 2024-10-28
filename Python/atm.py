balance = 1000
def atm():
    global balance
    action = input("Enter 'withdraw' or 'deposit': ")
    amount = int(input("Enter amount: "))
    if action == 'withdraw' and amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    elif action == 'deposit':
        balance += amount
        print("Deposit successful.")
    else:
        print("Insufficient funds.")
