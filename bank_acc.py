class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit


class Bank:
    def __init__(self) -> None:
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account_number):
        self.accounts = [acc for acc in self.accounts
                         if acc.account_number != account_number]

    def pay_dividend(self, dividend_amount):
        for account in self.accounts:
            account.deposit(dividend_amount)

    def update(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount) and account.balance < 0:
                print(f"Account {account.account_number}: You are in overdraft")


bank = Bank()

savings_acc = SavingsAccount("AF2252", 10000, 0.03)
current_acc = CurrentAccount("AD2001", 600, -2000)
normal_acc = Account("VR2555", 800)

bank.open_account(savings_acc)
bank.open_account(current_acc)
bank.open_account(normal_acc)

bank.update()
bank.pay_dividend(25)

print("After updates:")
for account in bank.accounts:
    print(f"Account {account.account_number} - Balance: {account.get_balance()}")

bank.close_account("AD2001")
print("After closing accont AD2001:")
for accont in bank.accounts:
    print(f"Account {accont.account_number} - Balance: {accont.get_balance()}")
