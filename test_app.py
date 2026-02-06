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
  assert mul(5, 2) == 10
  assert mul(10, 10) == 100
  print("Mul tests passed")

def testDiv():
  assert divide(10, 2) == 5
  assert divide(5, 0) == "Cannot divide by zero."
  assert divide(0, 5) == 0
  print("Div tests passed")

if __name__ == "__main__":
  testAdd()
  testMul()
  testSub()
  testDiv()
  print("All tests passed")
