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

# Entrada do usuario
valor1 = input("Digite o primeiro numero: ")
valor2 = input("Digite o segundo numero: ")
operador = input("Digite a operacao (+, -, *, /, ^): ")

# Validacao
if not is_valid_number(valor1) or not is_valid_number(valor2):
    print("None")
else:
    num1 = float(valor1)
    num2 = float(valor2)
    resultado = calcular(num1, num2, operador)

    if resultado is None:
        print("None")
    else:
        print("Resultado:", resultado)