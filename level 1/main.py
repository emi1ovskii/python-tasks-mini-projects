menu = {
    1: "deposit",
    2: "withdraw",
    3: "balance",
    4: "exit"
}
balance = 10
print("Choose your action:")
print("1. Deposit")
print("2. Withdraw")
print("3. Balance")
print("4. Exit")
while True:
    try:
        items = int(input("Choose your action: "))
    except ValueError:
        print("Please enter a number")
        continue

    if items not in menu:
        print("Invalid choice")
        continue



    if menu[items] == 'deposit':
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print("Successfully deposited ")

    elif menu[items] == 'balance':
        print(f"Your balance is {balance}")

    elif menu[items] == 'withdraw':
        amount = int(input("Enter the amount to withdraw: "))

        if amount > balance:
            print ("You don't have enough money`")
        else:
            balance -= amount
            print("Withdrawal successful")

    elif menu[items] == 'exit':
        print('You exited')
        break
