def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

input1 = int(input("Whats the first number? "))
input2 = int(input("Whats the second number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Choose an operation type: ")

func = operations[operation_symbol]
answer = func(input1, input2)

print(f"{input1} {operation_symbol} {input2} = {answer}")