# Importando as funções do calculadora.py
from calculadora import calcular, is_valid_number

# Solicitando ao usuário os valores de entrada
valor1 = input("Digite o primeiro número: ")
valor2 = input("Digite o segundo número: ")
operador = input("Digite a operação (+, -, *, /, ^): ")

# Validando se os valores de entrada são números válidos
if not is_valid_number(valor1) or not is_valid_number(valor2):
    print("None")
else:
    # Convertendo os valores de entrada para float
    num1 = float(valor1)
    num2 = float(valor2)
    
    # Realizando o cálculo
    resultado = calcular(num1, num2, operador)

    # Verificando se o resultado foi válido ou se deve retornar "None"
    if resultado is None:
        print("None")
    else:
        print(f"Resultado: {resultado}")
