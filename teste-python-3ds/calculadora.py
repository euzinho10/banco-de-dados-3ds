# calculadora.py

def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrai(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplica(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def divide(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")

    return a / b


def calcular(a, operador, b):
    """Executa uma operação matemática."""
    operacoes = {
        "+": soma,
        "-": subtrai,
        "*": multiplica,
        "/": divide,
    }

    if operador not in operacoes:
        raise ValueError(f"Operador inválido: {operador}")

    return operacoes[operador](a, b)
