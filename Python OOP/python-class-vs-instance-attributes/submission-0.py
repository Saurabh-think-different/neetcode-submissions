class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
alice_ba = BankAccount("Alice", 1000)
bob_ba = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${alice_ba.balance}")
print(f"Bob's balance: ${bob_ba.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
