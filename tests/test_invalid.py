import pytest
from dataAndFunctions.data import Data
from dataAndFunctions.functions import set

def test_1(set):
    set.enter_password(Data.not_containing_at_least_2_letters)
    set.click_button()
    text = set.text_message()
    assert Data.not_containing_at_least_2_letters_statement in text

def test_2(set):
    set.enter_password(Data.not_containing_at_least_1_number)
    set.click_button()
    text = set.text_message()
    assert Data.not_containing_at_least_1_number_statement in text

def test_3(set):
    set.enter_password(Data.not_containing_at_least_1_special_char)
    set.click_button()
    text = set.text_message()
    assert Data.not_containing_at_least_1_special_char_statement in text

def test_4(set):
    set.enter_password(Data.short_password)
    set.click_button()
    text = set.text_message()
    assert Data.short_password_statement in text

def test_5(set):
    set.enter_password(Data.long_password)
    set.click_button()
    text = set.text_message()
    assert Data.long_password_statement in text

def test_6(set):
    set.enter_password(Data.not_containing_at_least_1_uppercase)
    set.click_button()
    text = set.text_message()
    assert Data.not_containing_at_least_1_uppercase_statement in text

def test_7(set):
    set.enter_password(Data.not_containing_at_least_1_lowercase)
    set.click_button()
    text = set.text_message()
    assert Data.not_containing_at_least_1_lowercase_statement in text

def test_8(set):
    set.enter_password(Data.has_repeated_sequences)
    set.click_button()
    text = set.text_message()
    assert Data.has_repeated_sequences_statement in text
