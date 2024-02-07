def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculadora():
    num1 = float(input("what's the first number?"))
    calculating = True
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    for symbol in operations:
        print(symbol)
    while calculating:
        operation_symbol = input("what's the operations you chose?")
        calculate = operations[operation_symbol]
        num2 = float(input("what's the next number?"))
        answer = calculate(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculating = input(
            "Do you want to continue with the result? If so, type 'y'. If you want to continue "
            "from 0, type 'r'. To exit press another key.")
        if continue_calculating != "y" and continue_calculating != "r":
            calculating = False
        elif continue_calculating == "r":
            calculadora()
        else:
            num1 = answer


calculadora()
