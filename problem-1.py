class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

    if op == "add":
        print("Result:", calc.add(a, b))
    elif op == "subtract":
        print("Result:", calc.subtract(a, b))
    elif op == "multiply":
        print("Result:", calc.multiply(a, b))
    elif op == "divide":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid operation!")
