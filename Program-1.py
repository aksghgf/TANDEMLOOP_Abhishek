class Calculator:
    def operate(self, a, b, operation):
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Invalid operation"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

calc = Calculator()
print("Result:", calc.operate(a, b, operation))
