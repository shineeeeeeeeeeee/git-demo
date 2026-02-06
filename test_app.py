import pytest
from app import add, sub, mul, divide

def testAdd():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  print("Add tests passed")

def testSub():
  assert sub(5, 2) == 3
  assert sub(10, 10) == 0
  print("Sub tests passed")

def testMul():
  assert sub(5, 2) == 10
  assert sub(10, 10) == 100
  print("Mul tests passed")

def testDiv():
  assert div(10, 2) == 5
  assert div(5, 0) == "Cannot divide by zero."
  assert div(0, 5) == 0
  print("Div tests passed")

if __name__ == "__main__":
  testAdd()
  testMul()
  testSub()
  testDiv()
  print("All tests passed")
