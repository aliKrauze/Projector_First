from unittest.mock import patch
import pytest
from bank_acc import Bank, SavingsAccount, CurrentAccount, Account


def test_update_method():
    bank = Bank()

    savings_acc = SavingsAccount("SAV3333", 1000, 0.08)
    current_acc = CurrentAccount("CUR8888", 1500, -400)
    normal_acc = Account("NOR7787", 500)

    bank.open_account(savings_acc)
    bank.open_account(current_acc)
    bank.open_account(normal_acc)

    with patch("builtins.print") as mock_print:
        bank.update()

        assert savings_acc.get_balance() == 1080.0

        mock_print.assert_not_called()
