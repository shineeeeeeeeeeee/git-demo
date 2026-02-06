def add(a, b):
  a + b

def sub(a, b):
  a - b

def mul(a, b):
  a * b

def divide(a, b):
  if b == 0:
    return "Cannot divide by zero."
  return a / b

if __name__ == "__main__":
  print("Calculator App")
  print(f"10 + 5 = {add(10, 5)}")
  print(f"10 - 5 = {sub(10, 5)}")
  print(f"10 * 5 = {mul(10, 5)}")
  print(f"10 / 5 = {divide(10, 5)}")
    
