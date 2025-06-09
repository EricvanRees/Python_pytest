import pytest

import source.my_functions as my_functions

# 1. examples of function based tests
# run in terminal to test functions: "pytest tests/test_my_functions.py"

def test_add():
  result =  my_functions.add(number_one=1, number_two=4)
  """
  In Python, "assert" is a debugging aid that tests a condition as an aid to debugging. If the condition is true, the program continues executing as if nothing happened. If the condition is false, an assertion error exception is raised which interrupts the normal flow of the program. 
  """
  assert result == 5
  
def test_add_strings():
  result = my_functions.add(number_one="I like ", number_two="burgers")
  assert result == 'I like burgers'


def test_divide():
  result =  my_functions.divide(number_one=10, number_two=5)
  assert result == 2
  

def test_divide_by_zero():
  """this tells Python you're expecting a ValueError even though the function fails or there's an error in the function"""
  with pytest.raises(ValueError):
    result = my_functions.divide(number_one=10, number_two=0)