import pytest
from dataAndFunctions.data import Data
from dataAndFunctions.functions import set

def test_valid(set):
    set.enter_password(Data.valid)
    set.click_button()
    text = set.text_message()
    assert Data.valid_statement in text
