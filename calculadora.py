def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return None
        return num1 / num2
    elif operador == '^':
        return num1 ** num2
    else:
        return None
