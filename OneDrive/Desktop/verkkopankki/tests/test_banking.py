import sys
import os

# Lisää projektin juurikansio moduulien hakupolkuun
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from banking import BankAccount

import pytest

@pytest.fixture
def test_account():
    return BankAccount(username="testi", password="salasana", balance=100)

def test_login_success(test_account):
    assert test_account.login("testi", "salasana") == True

def test_login_failure(test_account):
    assert test_account.login("wrong_user", "salasana") == False
    assert test_account.login("testi", "wrong_password") == False

def test_deposit_success(test_account):
    assert test_account.deposit(50) == True
    assert test_account.get_balance() == 150

def test_deposit_failure(test_account):
    assert test_account.deposit(-50) == False

def test_withdraw_success(test_account):
    assert test_account.withdraw(50) == True
    assert test_account.get_balance() == 50

def test_withdraw_failure(test_account):
    assert test_account.withdraw(200) == False
    assert test_account.withdraw(-50) == False
