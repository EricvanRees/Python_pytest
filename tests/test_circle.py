import pytest
import source.shapes as shapes
import math

"""
class-based tests come with two useful functions:
1) setup method to run setup code before each test
2) tear down method to run tear down code after each test 
"""

class TestCircle:
  
  """
  to add the print function of both functions, add -s to command line, so:
  pytest -s tests/test_circle.py
  
  """
  def setup_method(self, method):
    print(f"Setting up {method}")
    self.circle = shapes.Circle(10)
    
  def teardown_method(self, method):
    print(f"Tearing down {method}")
    del self.circle
  
  def test_area(self):
    assert self.circle.area() == math.pi * self.circle.radius ** 2
  
  def test_perimeter(self):
    result = self.circle.perimeter()
    expected = 2 * math.pi * self.circle.radius
    assert result == expected
    
   