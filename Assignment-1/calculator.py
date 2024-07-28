def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    print("Simple Calculator")
    print("Add: ", add(1, 2))
    print("Subtract: ", subtract(5, 3))
    print("Multiply: ", multiply(4, 3))
    print("Divide: ", divide(10, 2))
    print("Divide by zero: ", divide(10, 0))
