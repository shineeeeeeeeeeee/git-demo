def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

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
