import pytest


def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)




# import pytest
# from wallet import Wallet, InsufficientAmount


# def test_default_initial_amount():
#     wallet = Wallet()
#     assert wallet.balance == 0

# def test_setting_initial_amount():
#     wallet = Wallet(100)
#     assert wallet.balance == 100

# def test_wallet_add_cash():
#     wallet = Wallet(10)
#     wallet.add_cash(90)
#     assert wallet.balance == 100

# def test_wallet_spend_cash():
#     wallet = Wallet(20)
#     wallet.spend_cash(10)
#     assert wallet.balance == 10

# def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
#     wallet = Wallet()
#     with pytest.raises(InsufficientAmount):
#         wallet.spend_cash(100)