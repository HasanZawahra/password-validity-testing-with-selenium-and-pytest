import pytest
from dataAndFunctions.setup import Setup


@pytest.fixture
def set():
    set = Setup(driver=Setup.driver)
    set.clear_password()
    return set
