"""
Exemplo do padrão Interpreter em Python com:
- Árvores sintáticas simples
"""

from abc import ABC, abstractmethod


# =======================================================
# Interface da Expressão (Nonterminal / Terminal)
# =======================================================

class Expression(ABC):
    """
    Interface base para todas as expressões da gramática.
    """

    @abstractmethod
    def interpret(self) -> int:
        """
        Avalia a expressão e retorna o resultado inteiro.
        """
        pass


# =======================================================
# Expressões Terminais
# =======================================================

class Number(Expression):
    """
    Representa um número literal na expressão.
    """

    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value


# =======================================================
# Expressões Não Terminais (Operadores)
# =======================================================

class Add(Expression):
    """
    Representa uma soma entre duas expressões.
    """

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        # Delegação clara: cada lado interpreta a si mesmo.
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    """
    Representa uma subtração entre duas expressões.
    """

    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()


# =======================================================
# Exemplo de Uso
# =======================================================

if __name__ == "__main__":
    # Expressão: 10 + (5 - 2)
    expression = Add(
        Number(10),
        Subtract(Number(5), Number(2))
    )

    result = expression.interpret()
    print(f"Resultado da expressão: {result}")
