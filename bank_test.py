from bank_acc import Bank, Account


def test_open_account():
    bank = Bank()

    account_number = "AWW5555"
    initial_balance = 2500
    bank.open_account(Account(account_number, initial_balance))

    assert len(bank.accounts) == 1

    opened_account = bank.accounts[0]
    assert opened_account.get_balance() == initial_balance
    assert opened_account.account_number == account_number
