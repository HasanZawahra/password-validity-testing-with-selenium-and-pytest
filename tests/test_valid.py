import pytest
from dataAndFunctions.data import Data
from dataAndFunctions.setup import Setup

def test_valid():
    set = Setup(driver=Setup.driver)
    set.clear_password()
    set.enter_password(Data.valid)
    set.click_button()
    text = set.text_message()
    assert Data.valid_statement in text
