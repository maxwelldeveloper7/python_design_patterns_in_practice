from __future__ import annotations
from abc import ABC, abstractmethod


# =============================================================
# STRATEGY — Interface para algoritmos intercambiáveis
# =============================================================
class ShippingStrategy(ABC):
    """
    Interface que define o algoritmo de cálculo de frete.
    Permite substituir estratégias de forma flexível.
    """

    @abstractmethod
    def calculate(self, weight: float) -> float:
        """Calcula o valor do frete."""
        pass


# =============================================================
# CONCRETE STRATEGIES — Implementações do algoritmo
# =============================================================
class SedexStrategy(ShippingStrategy):
    """Cálculo para o serviço de frete Sedex."""

    def calculate(self, weight: float) -> float:
        # Taxa fixa + taxa variável por quilo
        return 20.0 + (weight * 5.0)


class PACStrategy(ShippingStrategy):
    """Cálculo para o serviço PAC."""

    def calculate(self, weight: float) -> float:
        # Frete mais barato, porém mais lento
        return 10.0 + (weight * 2.0)


class TransportadoraStrategy(ShippingStrategy):
    """Cálculo de empresa transportadora."""

    def calculate(self, weight: float) -> float:
        # Geralmente mais caro, porém com seguro incluso
        return 30.0 + (weight * 3.0)


# =============================================================
# CONTEXT — Usa uma estratégia, mas não depende de detalhes internos
# =============================================================
class ShippingCalculator:
    """
    Contexto que utiliza uma estratégia de cálculo de frete.
    Permite a troca dinâmica da estratégia conforme necessidade.
    """

    def __init__(self, strategy: ShippingStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy) -> None:
        """Altera a estratégia em tempo de execução."""
        self._strategy = strategy

    def calculate_price(self, weight: float) -> float:
        """
        Delegação para a estratégia.
        O Context não sabe COMO o valor é calculado.
        """
        return self._strategy.calculate(weight)


# =============================================================
# Exemplo de uso
# =============================================================
if __name__ == "__main__":
    calculator = ShippingCalculator(SedexStrategy())

    print("Frete via Sedex:", calculator.calculate_price(5))

    calculator.set_strategy(PACStrategy())
    print("Frete via PAC:", calculator.calculate_price(5))

    calculator.set_strategy(TransportadoraStrategy())
    print("Frete via Transportadora:", calculator.calculate_price(5))
